from django.http import HttpResponse
import requests

url="http://localhost:4000/"

def inicio(request):
    traer()
    return HttpResponse("Hola")

def traer():
  y=request.get(url+'nombre')
  print(y.text)