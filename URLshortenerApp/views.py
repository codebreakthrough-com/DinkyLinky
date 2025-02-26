from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>home</h1>')

def helloWorld(request):
    return HttpResponse('<h1>helloWorld</h1>')
