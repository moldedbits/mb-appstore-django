from django.shortcuts import render
from django.http import HttpResponse
from .models import AppResource

def index(request):
    return HttpResponse("Hello, world. You're at the ios index.")

def all_resources(request):
	r_list = AppResource.objects.all()
	output = ', '.join([q.resource_key for q in r_list])
	return HttpResponse(output)
