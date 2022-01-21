from django.shortcuts import render

from .forms import RegistrationForm
from django.http import HttpResponseRedirect


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'authenticate/register.html', {'form': form})
