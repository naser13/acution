from django.http import HttpResponse
from django.shortcuts import render, redirect
from acution.commerce.forms import MemberForm,AddGoodForm
from acution.commerce.models import *

def home(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemberForm()
    return render(request, 'base.html', {'form': form})

def get(request):
    user = Member.objects.get(first_name='ansari')
    # price = Good.objects.all()
    g = Good.objects.get(owner = user)
    return HttpResponse(g)

def addGood(request):
    if request.method =='POST':
        form = AddGoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddGoodForm()
    return render(request,'addGood.html',{'form' : form})