from django.contrib import admin

# Register your models here.
from shop_app.models import Seller, Instrument, Product, Photo
from school.models import Teacher

admin.site.register(Seller)
admin.site.register(Instrument)
admin.site.register(Product)
admin.site.register(Photo)
admin.site.register(Teacher)
