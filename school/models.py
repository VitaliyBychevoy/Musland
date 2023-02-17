from django.db import models


class Teacher(models.Model):
    teachers_name = models.TextField(max_length=20)
    country = models.TextField(max_length=20, blank=True, default='Ukraine', null=True)
    city = models.TextField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    facebook_link = models.CharField(max_length=100, blank=True, null=True)
    telegram_link = models.CharField(max_length=50, blank=True, null=True)
    instagram_link = models.CharField(max_length=50, blank=True, null=True)
    price = models.CharField(max_length=250)
    info = models.TextField()
    speciality = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.teachers_name} {self.city} {self.phone}"
