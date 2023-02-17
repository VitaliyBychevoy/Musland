from django.shortcuts import render
from shop_app.models import Seller, Category

# Create your views here.
def index(request):
    return render(request, "menu_app/index.html")


def find_an_instrument(request):
    category = Category.objects.all()
    context = {"category_list": category}
    return render(request, "shop_app/categories.html", context)


def find_a_teacher(request):
    return render(request, 'school/find_teacher.html')
