from django.shortcuts import render
from django.views import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from .forms import CalcForm
from .models import Calculation
from rest_framework import status
from .serializers import CalculationSerializer
from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


class CalculatorView(View):

    def get(self, request):
        calc_form = CalcForm()
        context = {'calc_form': calc_form}
        return render(request, 'common_calc/main.html', context)

    def post(self, request):
        result = None
        calc_form = CalcForm(request.POST)

        if calc_form.is_valid():
            data = calc_form.cleaned_data
            if data['math_operation'] == 'AD':
                result = data['operand_1'] + data['operand_2']
            elif data['math_operation'] == 'SU':
                result = data['operand_1'] - data['operand_2']
            elif data['math_operation'] == 'MU':
                result = data['operand_1'] * data['operand_2']
            elif data['math_operation'] == 'DI':
                result = data['operand_1'] / data['operand_2']

            calc_obj = Calculation(
                person=request.user,
                operand_1=data['operand_1'],
                operand_2=data['operand_2'],
                math_operation=data['math_operation'],
                result=result,
            )
            calc_obj.save()
        result = round(result, 20)
        context = {'calc_form': calc_form,
                   'result': result,
                   }
        return render(request, 'common_calc/main.html', context)


class HistoryView(View):

    def get(self, request):
        if request.user.is_authenticated:
            calcs = Calculation.objects.filter(person=request.user)
            context = {'calcs': calcs}
            return render(request, 'common_calc/history.html', context)
        else:
            return HttpResponseRedirect('/calculator')


class CalculatorAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CalculationSerializer

    def post(self, request, *args, **kwargs):
        data_to_send_back = {}
        serializer = CalculationSerializer(data=request.data)
        data = request.data
        if serializer.is_valid():
            result = None
            if data['math_operation'] == 'AD':
                result = data['operand_1'] + data['operand_2']
            elif data['math_operation'] == 'SU':
                result = data['operand_1'] - data['operand_2']
            elif data['math_operation'] == 'MU':
                result = data['operand_1'] * data['operand_2']
            elif data['math_operation'] == 'DI':
                result = data['operand_1'] / data['operand_2']
            serializer.save(request, result)
            data_to_send_back['result'] = result
            return Response(data_to_send_back, status=status.HTTP_200_OK)
        else:
            data_to_send_back = serializer.errors
            return Response(data_to_send_back)


class HistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data_to_send_back = {}
        calcs = Calculation.objects.filter(person=request.user)
        data_to_send_back['calcs'] = calcs
        return Response(data_to_send_back, status=status.HTTP_200_OK)


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
