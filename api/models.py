from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=50, verbose_name='Покупатель', unique=True)


class Deal(models.Model):
    customer = models.ForeignKey('api.Customer', on_delete=models.CASCADE, verbose_name='Покупатель')
    item = models.CharField(max_length=50, verbose_name='Драг.камень')
    total = models.IntegerField(verbose_name='Стоимость')
    quantity = models.IntegerField(verbose_name='Количество')
    date = models.DateTimeField(verbose_name='Дата покупки')

