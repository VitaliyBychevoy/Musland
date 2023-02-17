from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15, null=True)
    facebook_link = models.CharField(max_length=100, blank=True, null=True)
    telegram_link = models.CharField(max_length=50, blank=True, null=True)
    instagram_link = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    type_instrument = models.CharField(max_length=50)


class Instrument(models.Model):
    sub_instrument = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'instruments'

    def __str__(self):
        return f"{self.sub_instrument} {self.category}"


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    country = models.CharField(max_length=30, null=True, default="Ukraine")
    city = models.CharField(max_length=30, null=True)
    message = models.TextField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return f"{self.title} {self.price}."


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField(null=True, default=None)
    photo = models.ImageField(null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.description}"
