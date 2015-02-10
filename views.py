from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from blog.models import BlogPosts

# Create your views here.


'''
def index(request):
	return HttpResponse("Hello, world. You're at the Blog")



def testing(request, number):
	return HttpResponse("This is the request, with %s" % number)

'''


def Posts(request, entry_id):
		posts = get_object_or_404(BlogPosts, pk=entry_id)
		return render(request, 'blog/posts.html', {'posts': posts})


def index(request):
	posts = BlogPosts.objects.order_by('-id')[:5]
	template = loader.get_template('blog/index.html')
	context = RequestContext(request, {
		'posts': posts,
	})
	return HttpResponse(template.render(context))
