from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('quiz/<int:id_usuario>/', views.quiz, name='quiz'),
    path('resultado/', views.resultado, name='resultado'),
    path('termo/', views.termo, name='termo'),
    path('captcha/', include('captcha.urls'))
]
