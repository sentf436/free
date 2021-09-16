from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Product(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=90, decimal_places=2)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title
