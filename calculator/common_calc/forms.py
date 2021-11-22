from django import forms
from .models import Calculation


class CalcForm(forms.ModelForm):
    class Meta:
        model = Calculation
        fields = ['operand_1', 'math_operation', 'operand_2']
