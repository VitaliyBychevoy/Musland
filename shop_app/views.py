import os, decimal
from django.shortcuts import render, redirect
from shop_app.models import Category, Instrument, Product, Seller, Photo
from .forms import SellerForm, CategoryForm, InstrumentForm, ProductForm
from musworld.settings import MEDIA_ROOT

def categories(request):
    #products = Product.objects.all()
    category = Category.objects.all()
    context = {'category_list': category}
    return render(request, "shop_app/categories.html", context)


def sell_instrument(request):

    return render(request, 'shop_app/sell_instrument.html')


def full_info_product(request):
    context = {}
    return render(request, "shop_app/product_info.html", context)


def instrument(request, category_id):
    category_by_id = Category.objects.get(id=category_id)
    instruments = Instrument.objects.filter(category=category_by_id).order_by('sub_instrument')
    context = {"list_instrument": instruments, "category_by_id": category_by_id}
    return render(request, "shop_app/instruments.html", context)


def products(request, instrument_id):
    instrument = Instrument.objects.get(id=instrument_id)
    products = Product.objects.filter(instrument=instrument).order_by('price')
    
    context = {"products": products, "instrument": instrument}
    return render(request, "shop_app/products.html", context)


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    photos = Photo.objects.filter(product=product)
    context = {"product": product, 'photos': photos}
    return render(request, "shop_app/product.html", context)


def new_seller(request):
    if request.method != "POST":
        form = SellerForm()
    else:
        form = SellerForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("all_sellers_name")
    context = {'form': form}
    return render(request, "shop_app/new_seller.html", context)


def all_sellers(request):
    sellers = Seller.objects.all()
    context = {"sellers": sellers}
    return render(request, "shop_app/all_sellers.html", context)


def delete_seller(request, seller_id):
    seller = Seller.objects.get(id=seller_id)
    seller.delete()
    sellers = Seller.objects.all()
    context = {"sellers": sellers}
    return render(request, "shop_app/all_sellers.html", context)


def update_seller(request, seller_id):
    seller = Seller.objects.get(id=seller_id)
    if request.method != "POST":
        form = SellerForm(instance=seller)
    else:
        form = SellerForm(instance=seller, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_sellers_name')
    context = {'seller': seller, 'form': form}
    return render(request, "shop_app/edit_seller.html", context)


def my_products(request, seller_id):
    seller = Seller.objects.get(id=seller_id)
    products = Product.objects.filter(seller=seller)
    context = {'products': products, 'seller': seller}
    return render(request, "shop_app/my_products.html", context)



def add_new_product(request, seller_id):
    seller = Seller.objects.get(id=seller_id)
    intstruments = Instrument.objects.all()
    categories = Category.objects.all()

    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')

        print("data: ", data)
        print("image: ", image)

        instrument = None

        if data['category'] != 'none' and data["instrument_new"] != 'none':
            print("Create new instrument ")
            category = Category.objects.get(id=data['category'])
            print(category)
            instrument = Instrument(sub_instrument=data["instrument_new"], category=category)
            print(instrument)
            instrument.save()
        else:
            instrument = Instrument.objects.get(id=data['instrument'])
        price = float(data['price'])
        product = Product(
            title=data["title"],
            price=price,
            country=data["country"],
            city=data['city'],
            message=data['message'],
            seller=seller,
            instrument=instrument,
        )
        print("title: ", product.title)
        print("price: ", product.price)
        print("country: ", product.country)
        print("city: ", product.city)
        print("message: ", product.message)
        print("seller: ", product.seller)
        print("instrument: ", product.instrument)
        product.save()

        photo = Photo.objects.create(
            product=product,
            description=data["description"],
            photo=image,
        )
        return redirect("my_products_name", seller_id)

    context = {
        'seller': seller,
        'instruments': intstruments,
        "categories": categories
    }
    return render(request, "shop_app/new_product.html", context)


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    s = product.seller
    photo = Photo.objects.get(product=product)
    path = photo.photo
    path_str = str(path)

    print(MEDIA_ROOT)
    p = (f"{MEDIA_ROOT}" + "\\" + path_str)
    product.delete()
    os.remove(p)
    return redirect("my_products_name", s.id)


def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)

    print("_$_$_$_" * 14)
    print(type(product.price))
    print(product.price)
    print("_$_$_$_" * 14)
    seller = product.seller
    instrument = product.instrument
    instrument_1 = instrument
    category = instrument.category
    photo = Photo.objects.get(product=product)
    instruments = Instrument.objects.all()

    if request.method == 'POST':

        data = request.POST

        image = request.FILES.get('image')


        instrument = None

        if data['category'] != 'none' and data["instrument_new"] != 'none':
            print("Create new instrument ")
            category = Category.objects.get(id=data['category'])
            instrument = Instrument(sub_instrument=data["instrument_new"], category=category)

            instrument.save()
            product.instrument = instrument,
        new_price = float(int(data['price']))
        print(" * " * 10)

        print(" * " * 10)

        product.title = data["title"],
        product.price = decimal.Decimal(new_price),
        product.country = data["country"],
        product.message = data["message"],
        product.save()

        photo = Photo.objects.filter(product=product)
        photo.description = data["description"]
        if image is not None:
            photo.photo = image
        photo.save()

        return redirect('product', product_id)

    context = {
        'product': product,
        'seller': seller,
        'instrument': instrument,
        'instruments': instruments,
        'category': category,
        'photo': photo,
    }
    return render(request, "shop_app/edit_product.html", context)
