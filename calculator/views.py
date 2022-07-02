from django.shortcuts import render
import math

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def plus(request):
    return render(request, 'plus.html')
    
def minus(request):
    return render(request, 'minus.html')
    
def prod(request):
    return render(request, 'product.html')
    
def quote(request):
    return render(request, 'quote.html')
    
def ruijo(request):
    return render(request, 'times.html')
    
def summation(request):
    try:
        val1 = float(request.POST['val1'])
    except ValueError as error:
        val1 = 0
    try:
        val2 = float(request.POST['val2'])
    except ValueError as error:
        val2 = 0
    answer = val1 + val2
    context = {
        'val1' : val1,
        'val2' : val2,
        'answer' : answer,
    }
    return render(request, 'index.html', context)
    
def difference(request):
    try:
        val1 = float(request.POST['val1'])
    except ValueError as error:
        val1 = 0
    try:
        val2 = float(request.POST['val2'])
    except ValueError as error:
        val2 = 0
    answer = val1 - val2
    context = {
        'val1' : val1,
        'val2' : val2,
        'answer': answer,
    }
    return render(request, 'index.html', context)
    
def product(request):
    try:
        val1 = float(request.POST['val1'])
    except ValueError as error:
        val1 = 0
    try:
        val2 = float(request.POST['val2'])
    except ValueError as error:
        val2 = 0
    answer = val1 * val2
    context = {
        'val1' : val1,
        'val2' : val2,
        'answer': answer,
    }
    return render(request, 'index.html', context)
    
def quotient(request):
    try:
        val1 = float(request.POST['val1'])
    except ValueError as error:
        val1 = 0
    try:
        val2 = float(request.POST['val2'])
    except ValueError as error:
        val2 = 0
    if val2!=0:
        answer = val1 / val2
    else:
        answer = "error"
    context = {
        'val1' : val1,
        'val2' : val2,
        'answer': answer,
    }
    if answer!="error":
        return render(request, 'index.html', context)
    else:
        return render(request, 'quote.html', context)
    
def times(request):
    try:
        val1 = float(request.POST['val1'])
    except ValueError as error:
        val1 = 0
    try:
        val2 = float(request.POST['val2'])
    except ValueError as error:
        val2 = 0
    answer = val1 ** val2
    context = {
        'val1' : val1,
        'val2' : val2,
        'answer': answer,
    }
    return render(request, 'index.html', context)

def about(request):
    try:
        val3 = int(request.POST.get('val3'))
    except ValueError as error:
        val3 = 0
    try:
        val4 = int(request.POST.get('val4'))
    except ValueError as error:
        val4 = 0
    result = math.gcd(val3, val4)
    bunsi = int(val3 / result)
    bunbo = int(val4 / result)
    context = {
        'val3' : val3,
        'val4' : val4,
        'bunsi' : bunsi,
        'bunbo' : bunbo,
    }
    return render(request, 'index.html', context)