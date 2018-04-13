from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('category/<slug>', views.category, name="category"),
    path('tag/<slug>', views.tag, name="tag"),
    path('<slug>', views.show, name="show"),
]
