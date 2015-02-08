from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from blog.models import BlogPosts

'''
def index(request):
	return HttpResponse("Hello, world. You're at the Blog")
'''


def testing(request, number):
	return HttpResponse("This is the request, with %s" % number)


def RecentPosts(request):
	posts = BlogPosts.objects.order_by('-BodyText')
	output = '<br> '.join([p.Title for p in posts]), '<br>', '<br> '.join([p.BodyText for p in posts])
	return HttpResponse(output)


def index(request):
	posts = BlogPosts.objects.order_by('-Title')[:5]
	template = loader.get_template('blog/index.html')
	context = RequestContext(request, {
		'posts': posts,
	})
	return HttpResponse(template.render(context))
