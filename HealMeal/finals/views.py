from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def home(request):
    return render(request, 'finals/HOME.html')

def index(request):
    return render(request, 'finals/index.html')

def about(request):
    return render(request, 'finals/about.html')

def component(request):
    return render(request, 'finals/Component.html')

def component1(request):
    return render(request, 'finals/Component1.html')

def component2(request):
    return render(request, 'finals/Component2.html')

def component3(request):
    return render(request, 'finals/Component3.html')

def bmi(request):
    return render(request, 'finals/FEATUREBMI.html')

def caremeal(request):
    return render(request, 'finals/FEATURECAREMEAL.html')

def caremeal1(request):
    return render(request, 'finals/FEATURECAREMEAL1.html')

def caremeal2(request):
    return render(request, 'finals/FEATURECAREMEAL2.html')

def fitness(request):
    return render(request, 'finals/FEATUREFITNESS.html')

def roulette(request):
    return render(request, 'finals/FEATUREROULETTE.html')

def features(request):
    return render(request, 'finals/features.html')

def gain(request):
    return render(request, 'finals/GAINWEIGHTRECIPES.html')

def join(request):
    return render(request, 'finals/Join.html')

def lose(request):
    return render (request, 'finals/LOSEWEIGHTRECIPES.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'finals/Join.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'finals/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'finals/logout.html')