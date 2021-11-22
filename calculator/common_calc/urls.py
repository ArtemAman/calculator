from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('calculator', views.CalculatorView.as_view(), name='calculator'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='calculator'), name='logout'),
    path('history', views.HistoryView.as_view(), name='history'),
    path('api/calculator', views.CalculatorAPIView.as_view()),
    path('api/history', views.HistoryAPIView.as_view()),
    url(r'^swagger(?P<format>\.json|\.yaml)$', views.schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', views.schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', views.schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
