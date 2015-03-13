from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from acution.commerce.forms import MemberForm, AddGoodForm


def home(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemberForm()
    return render(request, 'base.html', {'form': form})


def add_good(request):
    if request.method == 'POST':
        form = AddGoodForm(request.POST)
        if form.is_valid():
            good = form.save(commit=False)
            good.owner = request.user
            good.save()
            return redirect('home')
    else:
        form = AddGoodForm()
    return render(request, 'addGood.html', {'form': form})