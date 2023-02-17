from django import forms
from .models import Seller, Category, Instrument, Product


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = [
            'name',
            'phone',
            'facebook_link',
            'telegram_link',
            'instagram_link',
        ]
        labels = {
            'name': 'Name',
            'phone': 'Phone',
            'facebook_link': 'Facebook link',
            'telegram_link': 'Telegram link',
            'instagram_link': 'Instagram link'
        }
        widgets = {
            'facebook_link': forms.TextInput(attrs={'placeholder': ''}),

        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'type_instrument'
        ]
        labels = {
            'type_instrument': 'Category instrument'
        }


class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = [
            'sub_instrument'
        ]
        labels = {
            'sub_instrument': 'instrument'
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'country',
            'city',
            'message'
        ]
        labels = {
            'title': 'Title',
            'price': 'Price',
            'country': 'Country',
            'city': 'City',
            'message': 'Message',
        }
        widgets = {'message': forms.Textarea(attrs={'cols': 120})}
