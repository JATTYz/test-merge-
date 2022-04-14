from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def testView(request):
    announce = "We are going to code in this file !!!!"
    return HttpResponse(announce);