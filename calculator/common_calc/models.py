from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Calculation(models.Model):
    """ Модель для записи расчетов"""

    CHOICES = [
        ('AD', 'Addition'),
        ('SU', 'Subtraction'),
        ('MU', 'Multiplication'),
        ('DI', 'Division'),
    ]

    person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='person')
    operand_1 = models.FloatField(verbose_name='operand_1')
    operand_2 = models.FloatField(verbose_name='operand_2')
    math_operation = models.CharField(max_length=100, choices=CHOICES, verbose_name='math_operation', )
    result = models.FloatField(verbose_name='result')
    date = models.DateTimeField(default=timezone.now, verbose_name='date')

    class Meta:
        verbose_name = 'Calculation'
        verbose_name_plural = 'Calculations'
