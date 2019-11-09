from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   # path('addtwo',views.addtwo,name="addtwo")
    path('', views.default_page1),
    path('doit',views.doit,name='home'),
    path('add',views.add,name="add"),
    path('search',views.search,name="search"),
	path('addsongit1',views.addsongit,name="addsongit1"),
	path('delete',views.deleteit,name="delete"),
	path('update',views.updateit,name="update"),
	path('login',views.login,name="login"),
	path('register',views.register,name="register")
]