from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from chihuo.posts.models import Category
from chihuo.posts.models import Post
from django.contrib.sites.models import Site

def main_view(request):
	#request.session["nickname"] = "Jason"
	site_url = Site.objects.get_current().name
	return render_to_response('index/index.html',
		{
			'site_url'	:	site_url,
			#'name'		: 	request.session["nickname"],
		}
	)
	
def category_view(request,category):
	c = get_object_or_404(Category, id=category)	# get category
	return render_to_response('category/index.html',
		{
			'category_id'				:	c.id,
		}
	)


def search(request):
	query = request.GET.get('q', '')
	if query:
		qset = (
					Q(title__icontains=query)
		)
		results = Post.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response('index/search.html',
			{
				"results"	:	results,
				"query"		: 	query
			})
			
			
#extras
def join_us(request):
	return render_to_response('extras/join-us.html', {})
	
	