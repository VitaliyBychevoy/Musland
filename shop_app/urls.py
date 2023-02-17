from django.urls import path
from . import views
from menu_app import views as views_menu

urlpatterns = [
    path('', views.categories, name='categories'),
    path('<int:category_id>/', views.instrument, name='instrument'),
    path('?/<int:instrument_id>/', views.products, name='products'),
    path('?/?/<int:product_id>/', views.product, name='product'),
    path('index/', views_menu.index, name='index'),
    path('sell_instrument/', views.sell_instrument, name='sell_instrument_name'),
    path('new_seller/', views.new_seller, name='new_seller_name'),
    path('all_sellers/', views.all_sellers, name='all_sellers_name'),
    path('delete_seller/<int:seller_id>/', views.delete_seller, name='delete_seller_name'),
    path('update_seller/<int:seller_id>/', views.update_seller, name='update_seller_name'),
    path('my_products/<int:seller_id>/', views.my_products, name='my_products_name'),
    path('add_product/<int:seller_id>/', views.add_new_product, name='add_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name="del_prod"),
    path('update_product/<int:product_id>/', views.edit_product, name="edit_prod"),
    # path('cabinet/<int:seller_id>/', views.cabinet, name='cabinet_name'),

]
