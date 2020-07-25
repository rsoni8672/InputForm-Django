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
        input1  = request.POST.get('input1')
        input2  = request.POST.get('input2')
        input3  = request.POST.get('input3')
        input4  = request.POST.get('input4')
        #write your python function here 
        json={
                'name':["Rahul", "Rahul"]
        } 
        return render(request, "InputForm/output.html",json )
    return render(request, "InputForm/home.html")
