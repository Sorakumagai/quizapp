from django.urls import path
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('pref_quiz/', views.pref_quiz, name="pref_quiz"),
    path('pref_result/', views.pref_result, name="pref_result"),
    path('random_quiz/', views.random_quiz, name="random_quiz"),
    path('quiz_result/', views.quiz_result, name="quiz_result"),
    path('wiki/', views.wiki, name="wiki"),
    path('wiki_result/', views.wiki_result, name="wiki_result"),
]
