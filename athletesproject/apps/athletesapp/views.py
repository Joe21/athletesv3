from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response

from athletesproject.apps.athletesapp.models import Athlete
from athletesproject.apps.athletesapp.forms import AthleteForm

# from django.core import serializers
# from django.utils import simplejson
import json

def index(request):
	all_athletes = Athlete.objects.all()
	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'all_athletes' : all_athletes,
		})
	return HttpResponse(template.render(context))

def detail(request, athlete_id):
	# Find the athlete from the db using the id passed with the request
	athlete = Athlete.objects.get(pk=athlete_id)
	template = loader.get_template('detail.html')
	context = RequestContext(request, {
		'athlete' : athlete,
		})
	return HttpResponse(template.render(context))

def add(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = AthleteForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else:
			print form.errors
	
	else:
		form = AthleteForm()
	return render_to_response('add.html', { 'form' : form }, context)

def angular(request):
	template = loader.get_template('angular.html')
	context = RequestContext(request, {
		'all_athletes' : '',
		})
	return HttpResponse(template.render(context))

def data(request):
	data_array = []
	all_athletes = Athlete.objects.all()
	for athlete in all_athletes:
		data_array.append({ 'first_name': athlete.first_name, 'last_name': athlete.last_name, 'recommendation': athlete.recommendation })

	return HttpResponse(json.dumps(data_array))