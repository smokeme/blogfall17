from django.shortcuts import render, get_object_or_404
from .models import Post

def some_function(request):
	some_dictionary = {
		"some_key": "with a random value",
	}
	return render(request, "something.html", some_dictionary)


def post_list(request):
	objects = Post.objects.all()
	context = {
		"post_items": objects,
	}
	return render(request, "list.html", context)

def post_detail(request, post_id):
	# item = Post.objects.get(id=1000)
	item = get_object_or_404(Post, id=post_id)
	context = {
		"item": item,
	}
	return render(request, "detail.html", context)




