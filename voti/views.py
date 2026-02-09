from django.shortcuts import render

voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}

    
# Create your views here.
def view_a(request):
    materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]

    context={
        'materie':materie
    }
    return render(request, "view_a.html", context)

def view_b(request):
    context={
        'voti':voti
    }
    return render(request, "view_b.html", context)

def view_c(request):
    medie=[]

    for studente, dati in voti.items():
        media=0
        cont=0
        for materia, voto, assenze in dati:
            media+=voto
            cont+=1
        media/=cont
        medie.append((studente,media))

    context={
        'medie':medie
    }
    return render(request, "view_c.html", context)


#def view_d(request):