from django.contrib import admin
from .models import Calculation


class CalculationAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'operand_1', 'operand_2', 'math_operation', 'result', 'date']


admin.site.register(Calculation, CalculationAdmin)
