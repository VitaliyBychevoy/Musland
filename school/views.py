from django.shortcuts import render
from .models import Teacher


def find_teacher(request):
    return render(request, 'school/find_teacher.html')


def teach(request):
    return render(request, 'school/teach_login.html')


def find_speciality(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'school/find_speciality.html', context)