from django.shortcuts import render
from django.http import HttpResponse
from .models import IosApp
from django.template import loader

def index(request):
    return HttpResponse("Hello, world. You're at the ios index.")

def all_resources(request):
	r_list = IosApp.objects.all()
	template = loader.get_template('ios_app_list/index.html')
	context = {
        'latest_question_list': r_list,
    }
	return HttpResponse(template.render(context, request))
