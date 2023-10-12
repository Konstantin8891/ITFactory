from django.contrib import admin
from django.db import models

from users.models import User


class Shop(models.Model):
    name = models.CharField('Название', max_length=200)
    employee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='shops'
    )

    class Meta:
        unique_together = ('name', 'employee')
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'

    def __str__(self):
        return self.name

    @property
    @admin.display(description="Сотрудник",)
    def employee_name(self):
        return self.employee.name


class Visit(models.Model):
    date = models.DateTimeField('Дата посещения')
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name='visits'
    )
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'

    @property
    @admin.display(description="Сотрудник",)
    def employee(self):
        return self.shop.employee.name

    @property
    @admin.display(description="Торговая точка",)
    def shop_name(self):
        return self.shop.name
