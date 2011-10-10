from django import template
from django.db.models import get_model
from chihuo.posts.models import Category
from chihuo.posts.models import Post

register = template.Library()

# get_latest posts.post 5 as post_list
def get_latest(parser, token):
	bits = token.contents.split()
	if len(bits) != 5:
		raise TemplateSyntaxError, "get_latest tag takes exact four arguments"
	
	if bits[3] != 'as':
		raise TemplateSyntaxError, "third argument to the get_latest tag must be 'as' "
	return LatestContentNode(bits[1], bits[2], bits[4])
	
class LatestContentNode(template.Node):
	def __init__(self, model, num, varname):
		self.num, self.varname = num, varname
		self.model = get_model(*model.split('.'))
	
	def render(self, context):
		context[self.varname] = self.model._default_manager.all()[:self.num]
		return ''	

# get_posts_from_category 4 5 as post_list
def get_posts_from_category(parser, token):
	bits = token.contents.split()
	if len(bits)!= 5:
		raise TemplateSyntaxError, "get_posts_from_category tag takes exact five arguments"
	if bits[3] != 'as':
		raise TemplateSyntaxError, "fourth argument to the get_posts_from_category must be 'as'"
	return GetPostsFromCategory(bits[1], bits[2], bits[4])

#	bit[1] = category_id
#	bit[2] = number of posts
#   bit[4] = return variable
class GetPostsFromCategory(template.Node):
	def __init__(self, category, num, var_name):
		self.category_id = template.Variable(category)
		self.num = num
		self.var_name = var_name
		#self.category_id = category_id
		
	def render(self, context):
		actual_data = self.category_id.resolve(context)
		context[self.var_name] = Post.objects.filter(categories__id__contains=actual_data)
		return ''
	
class SubCategoryOf(template.Node):
	def __init__(self, parent_category_id, var_name):
		self.parent_category_id = parent_category_id
		self.var_name = var_name
	
	def render(self, context):
		context[self.var_name] = Category.objects.filter(parent__id=self.parent_category_id)
		return ''

def get_sub_category_of(parser, token):
	try:
		tag_name, parent_category_id,as_word, var_name= token.split_contents()
	except ValueError:
		msg = '%r tag requires a single argument' % token.contents[0]
		raise template.TemplateSyntaxError(msg)
	return SubCategoryOf(parent_category_id, var_name)

class GetCategoryOf(template.Node):
	def __init__(self, category_id, var_name):
		self.category_id = category_id
		self.var_name = var_name
	
	def render(self, context):
		context[self.var_name] = Category.obejcts.get(id=self.category_id)
		return ''

def get_category_of(parser, token):
	try:
		tag_name, category_id, as_word, var_name = token.split_contents()
	except ValueError:
		msg = '%r tag requires a single argument' % token.contents[0]
		raise template.TemplateSyntaxError(msg)
	return GetCategoryOf(category_id, var_name)


class GetSinglePost(template.Node):
	def __init__(self, post_id, var_name):
		self.post_id = post_id
		self.var_name = var_name
	
	def render(self, context):
		context[self.var_name] = Post.objects.get(id=self.post_id)
		return ''

def get_single_post(parser, token):
	try:
		tag_name, post_id, as_word, var_name = token.split_contents()
	except ValueError:
		msg = '%r tag requires a single argument' % token.contents[0]
		raise template.TemplateSyntaxError(msg)
	return GetSinglePost(post_id, var_name)

class GetLatestPost(template.Node):
	def __init__(self, var_name):
		self.var_name = var_name
	
	def render(self, context):
		context[self.var_name] = Post.objects.reverse().order_by('date')[0]
		return ''

def get_latest_post(parser, token):
	try:
		tag_name, as_word, var_name = token.split_contents()
	except ValueError:
		msg = '%r tag requires a single argument' % token.contents[0]
		raise template.TemplateSyntaxError(msg)
	return GetLatestPost(var_name)



register.tag('get_posts_from_category', get_posts_from_category)
register.tag('get_latest_post', get_latest_post)
register.tag('get_single_post', get_single_post)
register.tag('get_category_of', get_category_of)
register.tag('get_sub_category_of', get_sub_category_of)
register.tag('get_latest', get_latest)




