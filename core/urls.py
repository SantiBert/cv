from django.urls import path
from .views import IndexView, GalleryView, AllProjectsView, IndexAPIView, ProjectDetailAPIView, AllProjectsAPIView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('all-projects', AllProjectsView.as_view(), name='all-projects'),
    path('<slug:slug>/', GalleryView.as_view(), name='galeryimageslist'),
    path('api/index/', IndexAPIView.as_view(), name='api-index'),
    path('api/all-projects/', AllProjectsAPIView.as_view(), name='api-all-projects'),
    path('api/project/<slug:slug>/', ProjectDetailAPIView.as_view(), name='api-index'),
]
