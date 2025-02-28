from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from .views import URLViewSet

router = DefaultRouter()
router.register(r'urls', URLViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls))
]
