from django.urls import path
from . import views

app_name = "app2"

urlpatterns = [
    path('vista3/', views.vista3,name='vista3'),
    path('vista4/', views.vista4,name='vista4'),

]