from django.urls import path
from .views import IndexView, GaleryView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('mis-dibujos/',GaleryView.as_view(), name='galery')
]
