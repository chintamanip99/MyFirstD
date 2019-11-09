from django.db import models

# Create your models here.
class Album(models.Model):
	artist=models.CharField(max_length=200,default="")
	album_title=models.CharField(max_length=200,default="")
	genre=models.CharField(max_length=200,default="")
	album_logo=models.FileField()

	def __str__(self):
		return self.album_title

class Song(models.Model):
	album=models.ForeignKey(Album,on_delete=models.CASCADE,default="")
	file_type=models.CharField(max_length=100,default="")
	son_title=models.CharField(max_length=100,default="")
	son_logo=models.FileField()

	def __str__(self):
		return self.son_title
	

class Video(models.Model):
	son_title=models.ForeignKey(Song,on_delete=models.CASCADE,default="")
	file_type=models.CharField(max_length=100,default="")
	duration=models.CharField(max_length=100,default="")

class Users(models.Model):
	email=models.CharField(max_length=100,default="")
	username=models.CharField(max_length=100,default="")
	password=models.CharField(max_length=100,default="")




