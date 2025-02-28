from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from .views import URLViewSet

router = DefaultRouter()
router.register(r'urls', URLViewSet, basename='urls')

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('api/<str:short_code>', views.redirect_short, name='redirect_short'),  # Dynamic redirect
]
