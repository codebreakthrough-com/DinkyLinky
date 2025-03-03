from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse

from rest_framework import viewsets
from .models import URL
from .serializers import URLSerializer
from .helper import generate_short_url_rand


def home(request):
    return HttpResponse('<h1>home</h1>')


class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

    def perform_create(self, serializer):
        short_url = generate_short_url_rand()
        serializer.save(short_url=short_url)


def redirect_short(request, short_code):
    url_instance = get_object_or_404(URL, short_url=short_code)
    return redirect(url_instance.long_url)

