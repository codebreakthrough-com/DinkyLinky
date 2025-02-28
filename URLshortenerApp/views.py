from django.http import HttpResponse

from rest_framework import viewsets
from .models import URL
from .serializers import URLSerializer
from .red import generate_short_url

def home(request):
    return HttpResponse('<h1>home</h1>')

class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

    def perform_create(self, serializer):
        short_url = generate_short_url()
        serializer.save(short_url=short_url)
