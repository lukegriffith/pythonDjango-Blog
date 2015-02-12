from django.db import models

# Create your models here.


class BlogCategories(models.Model):
	category = models.CharField(max_length=75)
	dateFirstCreated = models.DateTimeField(auto_now=True, auto_now_add=True)

	def __unicode__(self):
		return self.category

	def count(self):
		return self.objects.all().count()

	class Meta:
		verbose_name_plural = "Categories"


class BlogPosts(models.Model):
	Title = models.CharField(max_length=200)
	BodyText = models.TextField()
	TimeStamp = models.DateTimeField(auto_now=True, auto_now_add=True)
	BlogCategroy = models.ForeignKey(BlogCategories)

	# Defining this so, when all method is ran it returns the title of the post
	def __unicode__(self):
		return self.Title

	class Meta:
		verbose_name_plural = "Blog Posts"


class AboutSite(models.Model):
	siteName = models.CharField(max_length=100)
	subtitle = models.CharField(max_length=250)
	Text = models.TextField()

	def __unicode__(self):
		return self.siteName

	class Meta:
		verbose_name_plural = "Information About the Site"
