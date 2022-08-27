from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=80, verbose_name='Имя')
    surname = models.CharField(max_length=80, verbose_name='Фамилия')
    age = models.PositiveIntegerField(verbose_name='Возраст', default=0, blank=True, null=True)
    image = models.ImageField(verbose_name='Фото', upload_to='Customers/%Y/%m/%d', blank=True, null=True)
    address = models.CharField(verbose_name='Адрес', max_length=80)

    def __str__(self):
        return f'{self.surname} {self.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        unique_together = ['name', 'surname']



