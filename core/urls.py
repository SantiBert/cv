from django.urls import path, include
from .views import IndexView, GalleryView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>/', GalleryView.as_view(), name='galeryimageslist'),
]
