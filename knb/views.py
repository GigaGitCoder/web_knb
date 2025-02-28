from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import User  # Импортируем модель User
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password, check_password
from random import choice
from django.views.decorators.csrf import csrf_exempt
import json
import base64
from django.core.files.base import ContentFile
import os
import cv2
import numpy as np
from .gesture_detector import GestureDetector
from django.db.models import F


# def sign_in_page(request):
#     if request.method == 'POST':
#         form = CustomAuthenticationForm(data=request.POST)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             login = cleaned_data.get('username')    
#             password = cleaned_data.get('password')
#         else:
#             print("Форма не валидна:")
#             print(form.non_field_errors())
#             print(form.errors, "fsdfds")
        
#         if form.is_valid():
#             if not login or not password:
#                 return render(request, 'signIn.html', {'error': 'Недостаточно данных', 'form': form})

#             user = authenticate(request, username=login, password=password)

#             # Проверяем, существует ли пользователь с таким логином и паролем
#             if user:
#                 response_data = {
#                     'login': login,
#                     'password': password
#                 }
#                 request.session['data'] = response_data
#                 return redirect('..')

#             return render(request, 'signIn.html', {'error': 'Неверный логин или пароль', 'form': form})

#     form = CustomAuthenticationForm()

#     return render(request, 'signIn.html', {'form': form})

def sign_in_page(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('..')
            else:
                return render(request, 'signIn.html', {'error': 'Неверный логин или пароль', 'form': form})
        else:
            return render(request, 'signIn.html', {'form': form})

    form = CustomAuthenticationForm()
    return render(request, 'signIn.html', {'form': form})

def sign_up_page(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():

            # Создаем нового пользователя
            user = form.save()
            login(request, user)
            return redirect('..') 
        else:
            return render(request, 'signUp.html', {'error': 'Некорректные данные', 'form': form})
        
        
    
    form = CustomUserCreationForm()
    
    return render(request, 'signUp.html', {'form': form})

def index_page(request):
    data = request.session.get('data')
    return render(request, 'index.html', context=data)

def game_page(request):
    if request.user.is_authenticated:
        # Получаем топ-10 игроков по количеству побед
        top_players = User.objects.order_by('-wins')[:10]
        return render(request, 'game.html', {'leaders': top_players})
    else:
        return redirect('../signin')

def logout_and_redirect(request):
    logout(request)
    return redirect('../signin')

def profile_page(request):
    if request.user.is_authenticated:
        total_games = request.user.wins + request.user.loses
        win_rate = (request.user.wins / total_games * 100) if total_games > 0 else 0
        context = {
            'user': request.user,
            'total_games': total_games,
            'win_rate': round(win_rate, 1)
        }
        return render(request, 'profile.html', context)
    else:
        return redirect('../signin')

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            image_data = data['image']

            # Убираем префикс "data:image/png;base64,"
            format, imgstr = image_data.split(';base64,') 
            ext = format.split('/')[-1]  # Получаем расширение файла

            # Декодируем base64 строку в бинарные данные
            image_binary = base64.b64decode(imgstr)
            
            # Преобразуем бинарные данные в numpy array для OpenCV
            nparr = np.frombuffer(image_binary, np.uint8)
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # Создаем экземпляр детектора жестов
            detector = GestureDetector("")
            
            # Определяем жест
            user_gesture = detector.detect_gesture(image)
            computer_gesture = choice(("Камень", "Бумага", "Ножницы"))

            user = User.objects.filter(username=request.user.username).first()

            if user_gesture != "Рука не обнаружена":
                if user_gesture == computer_gesture:
                    result = "Ничья"
                    user.update(games_total=F('games_total')+1)
                elif user_gesture == "Камень" and computer_gesture == "Ножницы" \
                or user_gesture == "Ножницы" and computer_gesture == "Бумага" \
                or user_gesture == "Бумага" and computer_gesture == "Камень":
                    result = "Вы победили!"
                    user.update(wins=F('wins')+1)
                    user.update(games_total=F('games_total')+1)
                else:
                    result = "Компьютер победил!"
                    user.update(loses=F('loses')+1)
                    user.update(games_total=F('games_total')+1)
            else:
                result = "Ошибка: рука не обнаружена"



            # Возвращаем результат
            print(result)
            # print(User.objects.filter(username=request.user.username).get('wins'))
            # print(User.objects.filter(username=request.user.username).get('loses'))
            return JsonResponse({
                'status': 'success',
                'user_gesture': user_gesture,
                'computer_gesture': computer_gesture,
                'result': result
            })

        except Exception as e:
            return JsonResponse({
                'status': 'error', 
                'message': str(e)
            }, status=400)
            
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request'
    }, status=400)

def send_scores(request):
    try:
        user = User.objects.filter(username=request.user.username).first()
        return JsonResponse({
                'status': 'success',
                'wins': str(user.wins),
                'loses': str(user.loses),
            })
    except Exception as e:
            return JsonResponse({
                'status': 'error', 
                'message': str(e)
            }, status=400)