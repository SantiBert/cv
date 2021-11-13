from django.urls import path
from .views import IndexView, GalleryView, AllProjectsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('all-projects', AllProjectsView.as_view(), name='all-projects'),
    path('<slug:slug>/', GalleryView.as_view(), name='galeryimageslist'),
]
