from django.shortcuts import render
from django.http import HttpResponse


from family.models import Family

def index(request):
    return render(request, 'index.html', context={})

def create_person(request):
    new_person = Family.objects.create(name= 'Federico Martin Diaz', age= 22, work= True, hobbie = "Lavar el auto")
    print(new_person)
    return HttpResponse('Nuevo integrante de la familia creado')

def list_family(request):
    all_family = Family.objects.all()
    print(all_family)
    context = {
        'personas':all_family,
    }
    return render(request, 'list_family.html', context=context)
    