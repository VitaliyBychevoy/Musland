from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.find_an_instrument, name='categories'),
    path('find_a_teacher/', views.find_a_teacher),
]


