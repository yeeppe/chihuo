from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from chihuo.people.models import Person

def login(request):
	if request.method == "POST":
		try:
			p = Person.objects.get(email__exact = request.POST['email'])
			if p:
				request.session['userid'] = p.id
				return render_to_response('index/index.html')
		except Person.DoesNotExist:
			return render_to_response('people/login.html', {'message' : "Incorrect Username/password!"})
	else:
		return render_to_response('people/login.html', context_instance = RequestContext(request))

def logout(request):
	try:
		del request.session['userid']
	except KeyError:
		pass
	return render_to_response('index/index.html')

def register(request):
	if request.method == "POST":
		submitted = NewUserRegistrationForm(request.POST)	# get submitted data
		if submitted.is_valid():
			#title = form.cleaned_data['title']
			return render_to_response('index/index.html',
				{
					'message'	: 'Welcome',
				}
			)
	else:
		newform = NewUserRegistrationForm()
		return render_to_response('people/register.html',
					{
						'form': newform,
					},
					context_instance = RequestContext(request)
		)
