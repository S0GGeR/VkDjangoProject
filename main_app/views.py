import requests
from django.shortcuts import render
from django.views.generic.base import View
from allauth.socialaccount.models import SocialToken


class AuthView(View):
    """Авторизация через социиальную сесть Вконтакте"""
    """Сперва достаем из базы данных access token пользователя.
    Далее через VK API отправляем запрос на получение пяти случайных 
    друзей. Ответ приходит в виде массива ID. При помощи него, уже используя 
    другой метод API,получаем подробную информацию о пользователях"""

    def get(self, request):
        profiles_info = ""
        if request.user.is_authenticated:
            token = SocialToken.objects.filter(account__user=request.user, account__provider='vk')
            friends_ids = requests.get(
                'https://api.vk.com/method/friends.get?v=5.52&count=5&order=random&access_token=' + str(token[0])
            )
            if friends_ids.status_code == 200 and 'response' in friends_ids.json():
                profiles = requests.get(
                    'https://api.vk.com/method/users.get?v=5.52&user_ids={ids}&fields=photo_100&access_token={token}'.format(
                        ids=str(friends_ids.json()['response']['items']).strip('[]'), token=token[0])
                )
                if profiles.status_code == 200 and 'response' in profiles.json():
                    profiles_info = profiles.json()['response']
                else:
                    return render(request, "error.html")
            else:
                return render(request, "error.html")
        return render(request, "index.html", {"profiles": profiles_info})
