from django.shortcuts import render
from django.http import HttpResponse
from one.models import Song,Album,Users
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User,auth 
# Create your views here.
def index(request):
   return HttpResponse('<h1>Yesss</h1>')

def doit(request):
   return render(request,'home.html',{'name':'Chintamani'})

def loginpage(request):
   return render(request,'login.html',{'message':'Welcome to the world of music'})

def search(request):
   query=request.POST['searchit']
   results = Song.objects.filter( Q(son_title__icontains=query))
   results2=Album.objects.filter(Q(artist__icontains=query)|Q(album_title__icontains=query))
   return render(request,'index.html',{'results':results,'results2':results2})

def deleteit(request):
   son_title_to_delete=request.GET['son_title111']
   Song.objects.filter(son_title=son_title_to_delete).delete()
   albumlist,songlist=Album.objects.all(),Song.objects.all()
   return render(request,'addsong.html',{'message':'Here Add Songs','albumlist':albumlist,'songlist':songlist})

def updateit(request):
   songname=request.POST['songname']
   newsongname=request.POST['newsongname']
   newsongfiletype=request.POST['newsongfiletype']
   newsongalbum=request.POST['newsongalbum']
   newsonglogo=request.POST['newsonglogo']
   sn=Song.objects.get(son_title=songname)
   sn.son_title=newsongname
   sn.file_type=newsongfiletype
   sn.son_logo=newsonglogo
   a1=Album.objects.filter(album_title=newsongalbum)
   a1[0].save()
   sn.album=a1[0]
   albumlist,songlist=Album.objects.all(),Song.objects.all()
   sn.save()
	#return HttpResponse('<h1>Yesss</h1>') 
   return render(request,'addsong.html',{'albumlist':albumlist,'songlist':songlist})

def login(request):
   username1=request.POST['username']
   password1=request.POST['password']
   Users.objects.filter(username=username1)

def register(request):
   email1=request.POST['email']
   username1=request.POST['username']
   password1=request.POST['password']
   Users(email=email1,username=username1,password=password1).save()
   return render(request,'login.html')

def default_page(request):
   return render(request,'index.html',{'message':'Welcome To The World Of Music!!!!'})

def default_page1(request):
   return render(request,'login.html',{'message':'Welcome To The World Of Music!!!!'})

def add(request):
   albumlist,songlist=Album.objects.all(),Song.objects.all()
   return render(request,'addsong.html',{'albumlist':albumlist,'songlist':songlist})

def addsong(request):
   albumlist,songlist=Album.objects.all(),Song.objects.all()
   return render(request,'addsong.html',{'message':'Here Add Songs','albumlist':albumlist,'songlist':songlist})

def addsongit(request):
	albumlist,songlist=Album.objects.all(),Song.objects.all()
	son_title1=request.POST['son_title'];
	file_type1=request.POST['file_type'];
	son_logo1=request.POST['son_logo'];
	album1=request.POST['album'];
	a1=Album.objects.filter(album_title=album1)
	a1[0].save()
	s1=Song(son_title=son_title1,file_type=file_type1,son_logo=son_logo1,album=a1[0])
	s1.save()
	#add(request)
	return render(request,'addsong.html',{'message':'Here Add Songs','albumlist':albumlist,'songlist':songlist})
	#return HttpResponse('<h1>Yesss</h1>')


	
	
 
#def addsongit(request):
	
