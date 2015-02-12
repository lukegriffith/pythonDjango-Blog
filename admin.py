from django.contrib import admin
from blogsite.models import BlogPosts, AboutSite, BlogCategories
# Register your models here.


class BlogCategoriesAdmin(admin.ModelAdmin):
	list_dispaly = ['category']

admin.site.register(BlogCategories, BlogCategoriesAdmin)


class BlogPostsAdmin(admin.ModelAdmin):
	list_display = ('Title', 'TimeStamp')
	list_filter = ['TimeStamp']

admin.site.register(BlogPosts, BlogPostsAdmin)


class AboutSiteAdmin(admin.ModelAdmin):
	list_display = ['siteName']

admin.site.register(AboutSite, AboutSiteAdmin)
