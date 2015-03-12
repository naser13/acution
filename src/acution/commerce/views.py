from django.shortcuts import render
from acution.commerce.forms import MemberForm


def home(request):
    form = MemberForm()
    return render(request, 'base.html', {'form': form})