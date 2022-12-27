from django.db import models

class BodyMassIndex(models.Model):
    BMI = models.CharField(max_length=50,null=True)

    class Meta:
        verbose_name = 'Индекс Массы Тела'
        verbose_name_plural = 'База ИМТ'

class Calories(models.Model):
    defg = models.CharField(max_length=50,null=True)

    class Meta:
        verbose_name = 'Дневное потребление калорий'
        verbose_name_plural = 'Дневное потребление калорий'


class Diet(models.Model):
    users = models.CharField(max_length=100, null=True)
    age = models.IntegerField(max_length=100, null=True)
    height = models.IntegerField(max_length=100, null=True)
    weight = models.IntegerField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    activity = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Общие сведения'
        verbose_name_plural = 'Общие сведения'