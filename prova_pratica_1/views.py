from django.shortcuts import render
import datetime
import random

def index(request):
    return render(request, "prova_pratica_1/index.html")

def differenza(request):
    var1=random.randint(1,20)
    var2=random.randint(1,20)
    var3=var1-var2
    context={
        'var1':var1,
        'var2':var2,
        'var3':var3
    }
    return render(request, "differenza.html", context)

def pari_dispari(request):
    listaNum=[]
    nPari=0
    nDisp=0
    for i in range(15):
        num=var1=random.randint(1,20)
        listaNum.append(num)
        if num%2==0:
            nPari+=1
        else:
            nDisp+=1

    context={
        'listaNum': listaNum,
        'nPari':nPari,
        'nDisp':nDisp
    }
    return render(request, "pari_dispari.html", context)