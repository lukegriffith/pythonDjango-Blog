from django.db import models

# Create your models here.

class BlogPosts(models.Model):
	Title = models.CharField(max_length=200)
	BodyText = models.TextField()
	TimeStamp = models.DateTimeField(auto_now=True,auto_now_add=True)


