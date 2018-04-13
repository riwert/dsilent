from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('category/<slug>', views.category, name="category"),
    path('<slug>', views.show, name="show"),
]
