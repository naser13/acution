from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from acution.commerce.forms import *
from acution.commerce.data import Data

def home(request):
    categories = Data.categories
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemberForm()

    return render(request, 'widg/user.html', {'form': form,'categories':categories})

@login_required(login_url='login')
def add_good(request):
    if request.method == 'POST':
        form = AddGoodForm(request.POST)
        pic_form = picture_form(request.POST, request.FILES)
        if form.is_valid() and pic_form.is_valid():
            good = form.save(commit=False)
            img = pic_form.save(commit=False)
            good.owner = request.user
            good.save()
            img.good = Good.objects.get(id=good.id)
            img.save()
            return redirect('home')
    else:
        form = AddGoodForm()
        pic_form = picture_form()
    return render(request, 'addGood.html', {'form': form,'pic_form':pic_form})
