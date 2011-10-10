# Create your views here.
from forms import RSVPCreateEventForm
from django.shortcuts import render_to_response
from django.template import Context
from django.template import RequestContext
from chihuo.rsvp.models import ChihuoEvent

def index(request):
	return render_to_response('rsvp/index.html', context_instance = RequestContext(request))

def create_event(request):
	if request.method == 'POST':
		submitted = RSVPCreateEventForm(request.POST)	# get submitted data
		if submitted.is_valid():
			title = form.cleaned_data['title']
			return render_to_response('rsvp/')
	else:
		newform = RSVPCreateEventForm()
		return render_to_response('rsvp/create-event.html',
				{
					'form': newform,
				},
				context_instance = RequestContext(request)
	)

def join(request):
	if "userid" in request.session:
		return render_to_response('rsvp/index.html',
			{
				'message'	: "Joined",
			})
	else:
		return render_to_response('rsvp/index.html',
			{
				'message'	: "Please log in first",
			},
			context_instance = RequestContext(request)
		)


