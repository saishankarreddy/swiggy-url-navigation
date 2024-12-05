from django.urls import path
from delivery.views import *
app_name ='delivery'
urlpatterns = [
    path('order/',order,name='order'),
]