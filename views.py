from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from blogsite.models import BlogPosts, AboutSite, BlogCategories

# Create your views here.


'''
def index(request):
	return HttpResponse("Hello, world. You're at the Blog")



def testing(request, number):
	return HttpResponse("This is the request, with %s" % number)

'''


def Posts(request, entry_id):
		posts = get_object_or_404(BlogPosts, pk=entry_id)
		about = get_object_or_404(AboutSite)
		categories = BlogCategories.objects.order_by('-category')
		objectList = {
			'posts': posts,
			'about': about,
			'categories': categories,
		}
		return render(request, 'blog/posts.html', objectList)


def index(request):
	posts = BlogPosts.objects.order_by('-id')[:5]
	about = get_object_or_404(AboutSite)
	template = loader.get_template('blog/index.html')
	categories = BlogCategories.objects.order_by('-category')
	context = RequestContext(request, {
		'posts': posts,
		'about': about,
		'categories': categories,
	})
	return HttpResponse(template.render(context))


def Categories(request, categoryChoice):
	posts = BlogPosts.objects.filter(BlogCategroy_id=categoryChoice)
	about = get_object_or_404(AboutSite)
	template = loader.get_template('blog/categories.html')
	categories = BlogCategories.objects.order_by('-category')
	categoryTitle = get_object_or_404(BlogCategories, pk=categoryChoice)
	context = RequestContext(request, {
		'posts': posts,
		'about': about,
		'categories': categories,
		'categoryTitle': categoryTitle,
	})
	return HttpResponse(template.render(context))
