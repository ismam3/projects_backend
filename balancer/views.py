from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .pychemist import Equation


def index(request,pk):
    if pk!=None:
        equation = Equation(str(pk))
        return HttpResponse(equation.balance())