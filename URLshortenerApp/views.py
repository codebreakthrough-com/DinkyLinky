from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from .models import URL
from .serializers import URLSerializer
from .helper import generate_short_url_rand, base62_encode, base62_decode


def home(request):
    return HttpResponse('<h1>home</h1>')


class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url_instance = serializer.save()

        b62 = base62_encode(url_instance.id)  # Generate short URL
        return Response({'short_url': b62}, status=status.HTTP_201_CREATED)


def redirect_short(request, short_code):
    decoded = base62_decode(short_code)
    url_instance = get_object_or_404(URL, id=decoded)
    return redirect(url_instance.long_url)

