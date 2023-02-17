from django.urls import path
from . import views
from menu_app import views as views_menu

urlpatterns = [
    path('', views.find_teacher, name='find_teacher_name'),
    path('teach/', views.teach, name='teach_name'),
    path('find_speciality/', views.find_speciality, name='speciality_name'),

]
