from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.landing,name='landing'),
    path("home",views.index,name='home'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("nearby",views.nearby,name='nearby'),
    path("dealer",views.dealer,name='dealer'),
    path("advice",views.advice,name='advice'),
    path("login",views.login,name='login'),
    path("signup",views.signup,name='signup'),
    path("logout",views.logout,name='logout'),
    path("sale",views.sale,name='sale'),
]

