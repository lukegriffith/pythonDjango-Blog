from django.contrib import admin
from blog.models import BlogPosts
# Register your models here.

class BlogPostsAdmin(admin.ModelAdmin):
	list_display = ('Title', 'TimeStamp')
	list_filter = [ 'TimeStamp']

admin.site.register(BlogPosts, BlogPostsAdmin)