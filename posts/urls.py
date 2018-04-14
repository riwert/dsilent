from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('category/<slug>', views.category, name="category"),
    path('tag/<slug>', views.tag, name="tag"),
    path('<slug>', views.show, name="show"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
