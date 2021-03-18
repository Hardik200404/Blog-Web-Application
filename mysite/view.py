from django.http import HttpResponse
def home(req):
    return HttpResponse('<h1>Hello</h1>')