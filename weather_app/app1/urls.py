from django.urls import path
from . import views
from .views import predict_weather
app_name='app1'
urlpatterns=[
    path('',views.index,name='index'),
    
    path('result',views.result,name='result'),
     path('predict/', predict_weather, name='predict_weather'),
   
]