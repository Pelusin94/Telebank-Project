from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from . import forms


def main_page(request):
    template = 'telebank/main.html'
    context = {}
    return render(request, template, context)

def user_login(request):
    template = 'telebank/login.html'
    form = forms.loginForm
    context = {
        'Login': form
    }

    if request.method == 'POST':
        if form.is_valid():
            form = forms.loginForm(request.POST)
            username = form['username']
            password = form['password']
            user = authenticate(username=username, password=password)

            if user.is_active:
                login(request,user)
                return redirect('')

    return render(request, template, context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('')



