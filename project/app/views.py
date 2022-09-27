from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import AtividadesForm
from app.models import Atividades


# Create your views here.
def home(request):
    data = {}
    data['db'] = Atividades.objects.all()
    return render(request, "index.html", data)

def form(request):
    data = {}
    data['form'] = AtividadesForm()
    return render(request, "form.html", data)

def create(request):
    form = AtividadesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request,pk):
    data = {}
    data['db'] = Atividades.objects.get(pk=pk)
    return render(request, "view.html", data)

def edit(request,pk):
    data = {}
    data['db'] = Atividades.objects.get(pk=pk)
    data['form'] = AtividadesForm(instance=data['db'])
    return render(request, "form.html", data)

def update(request,pk):
    data = {}
    data['db'] = Atividades.objects.get(pk=pk)
    form = AtividadesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save
        return redirect('home')

def delete(request,pk):
    db = Atividades.objects.get(pk=pk)
    db.delete()
    return redirect('home')