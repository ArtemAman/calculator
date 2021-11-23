# Generated by Django 3.2.9 on 2021-11-19 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_calc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='math_operation',
            field=models.CharField(choices=[('AD', 'Addition'), ('SU', 'Subtraction'), ('MU', 'Multiplication'), ('DI', 'Division')], max_length=100, verbose_name='math_operation'),
        ),
    ]
