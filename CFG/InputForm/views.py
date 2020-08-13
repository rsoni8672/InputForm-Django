from django.shortcuts import render
from InputForm.models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from CFG.settings import BASE_DIR, TEMPLATES
@csrf_exempt
def addcomplaint(request):
    print("Hello")    
    print(BASE_DIR)    
    print(TEMPLATES[0]['DIRS'])
    if request.method == "POST":
        x  = request.POST.get('input1').lower()
        d = {'a': 'v', 'b': 'k', 'c': 'j', 'd': 'r', 'e': 'x', 'f': 'o', 'g': 'n', 'h': 't', 'i': 'u', 'j': 'c', 'k': 'b', 'l': 'q', 'm': 'w',
     'n': 'g', 'o': 'f', 'p': 's', 'q': 'l', 'r': 'd', 's': 'p', 't': 'h', 'u': 'i', 'v': 'a', 'w': 'm', 'x': 'e', 'y': 'z', 'z': 'y', 
      ' ' : '_'}
        password = "X"
        
        #x = input().lower()
        for j in x:
                password += d[j]
        password += chr(64) + str(len(x)) + str(len(x) - 2) + chr(63) + str(len(x) + 3)
        print(password)

        
        #input2  = request.POST.get('input2')
        #input3  = request.POST.get('input3')
        #input4  = request.POST.get('input4')
        #write your python function here 
        json={
                'original': x,
                'password': password
        } 
        return render(request, "InputForm/output.html",json )
    return render(request, "InputForm/home.html")
