from .models import Calculation
from rest_framework import serializers


class CalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculation
        fields = ['operand_1', 'math_operation', 'operand_2', ]

    def save(self, request, result, *args, **kwargs, ):
        calc = Calculation(
            person=request.user,
            operand_1=self.validated_data['operand_1'],
            operand_2=self.validated_data['operand_2'],
            math_operation=self.validated_data['math_operation'],
            result=result,
        )

        calc.save()
