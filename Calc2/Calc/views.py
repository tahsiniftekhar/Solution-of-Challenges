from django.shortcuts import render
from django.http import HttpResponse

def sum(request, num1, num2):
    res = num1 + num2
    return render(request, 'result.html', {'result': res})

def sub(request, num1, num2):
    res = num1 - num2
    return render(request, 'result.html', {'result': res})
