# Generated by Django 4.0.8 on 2023-01-15 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='telegram_link',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
