"""
URL configuration for HealMeal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from django.contrib.auth import views as auth_views

from finals import views as finals_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('index/', finals_views.index, name='index'),
    path('index.html/', finals_views.index, name='index'),

    path('', finals_views.home, name='home'),

    path('about/', finals_views.about, name='about'),
    path('about.html/', finals_views.about, name='about'),

    path('component/', finals_views.component, name='component'),  
    path('Component/', finals_views.component, name='component'),  

    path('component1/', finals_views.component1, name='component1'),
    path('Component1.html/', finals_views.component1, name='component1'),  
    
    path('component2/', finals_views.component2, name='component2'),
    path('Component2.html/', finals_views.component2, name='component2'),

    path('component3/', finals_views.component3, name='component3'),
    path('component3.html/', finals_views.component3, name='component3'),
    
    path('bmi/', finals_views.bmi, name='bmi'),
    path('FEATUREBMI.html/', finals_views.bmi, name='bmi'),

    path('caremeal/', finals_views.caremeal, name='caremeal'),
    path('FEATURECAREMEAL.html/', finals_views.caremeal, name='caremeal'),

    path('caremeal1/', finals_views.caremeal1, name='caremeal1'),
    path('FEATURECAREMEAL1.html/', finals_views.caremeal1, name='caremeal1'),

    path('caremeal2/', finals_views.caremeal2, name='caremeal2'),
    path('FEATURECAREMEAL2.html/', finals_views.caremeal2, name='caremeal2'),

    path('fitness/', finals_views.fitness, name='fitness'),
    path('FEATUREFITNESS.html/', finals_views.fitness, name='fitness'),

    path('roulette/', finals_views.roulette, name='roulette'),
    path('FEATUREROULETTE.html/', finals_views.roulette, name='roulette'),

    path('features/', finals_views.features, name='features'),
    path('features.html/', finals_views.features, name='features'),

    path('gain/', finals_views.gain, name='gain'),
    path('GAINWEIGHTRECIPES.html/', finals_views.gain, name='gain'),

    path('join/', finals_views.join, name='join'),
    path('Join.html/', finals_views.join, name='join'),

    path('lose/', finals_views.lose, name='loss'),
    path('LOSEWEIGHTRECIPES.html', finals_views.lose, name='loss'),

    path('join/', finals_views.join, name='register'),
    path('login/', finals_views.login_view, name='login'),
    path('logout/', finals_views.logout_view, name='logout'),

    # path('register/', finals_views.register, name='register'),

    # path('login/', auth_views.LoginView.as_view(template_name='finals/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='finals/logout.html'), name='logout'),
]
