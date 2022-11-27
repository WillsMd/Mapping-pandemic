from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout, authenticate, login
import json
from django.views.decorators.csrf import csrf_exempt
from . import forms
# Create your views here.

def home(request):
    return render(request, 'index.html')


def index(request):
    if request.user.is_authenticated:
        
        return render(request, "home.html")
    else:
        return redirect("login")

def login(request):
    if request.method == 'POST':
        form = forms.Login(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:

                return render(request, "home.html")
        else:
            return render(request = request,
                    template_name = "login.html",
                    context={"form":form,"error":"Incorrect Username or Password"})
    form = forms.Login()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

def logout(request):
    auth.logout(request)
    return redirect('home')

def register(request):
    if request.method == "POST":
        form = forms.Registration(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            return redirect("login")

        return render(request = request,
                          template_name = "register.html",
                          context={"form":form})
    form = forms.Registration()
    return render(request = request,
                  template_name = "register.html",
                  context={"form":form})
        
import pandas as pd 
        
def predict(request):
    if request.method == "POST":
        
        Symptom_one = request.form['Symptom_one']
        Symptom_two = request.form['Symptom_two']
        Symptom_three = request.POST['Symptom_three']
        Symptom_four = request.POST['Symptom_four']
        Symptom_five = request.POST['Symptom_five']
        Symptom_six = request.POST['Symptom_six']

    
    arr = [[Symptom_one, Symptom_two, Symptom_three, Symptom_four, Symptom_five, Symptom_six]]
    df = pd.DataFrame(arr, columns=['Symptom_one', 'Symptom_two', 'Symptom_three','Symptom_four','Symptom_five','Symptom_six'])
    print(arr)

    pred = model.predict(df)
    return render_template('home.html', predicted=pred[0]) 