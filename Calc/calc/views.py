from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def calc(request):
    x = int(request.POST["num1"])
    y = int(request.POST["num2"])
    operator = request.POST["sign"]

    # if x or y == "None":
    #     result: "Insert Value!!!"

    if "add" in operator:
        result = x + y

    elif "dif" in operator:
        result = x - y

    elif "mult" in operator:
        result = x * y

    elif "div" in operator:
        result = x / y  

    return render(request, 'result.html', {'result': result})

