from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def showIndex(http_request):
    message = "Hello world"
    return HttpResponse(message)
