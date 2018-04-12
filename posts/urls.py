from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<slug>', views.show, name="show"),
]
