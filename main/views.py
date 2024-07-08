from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request): 

	profiles = Profile.objects.all()

	# fcontent = Service.objects.all()[0] # first content
	# scontent = Service.objects.all()[1] # second content
	# tcontent = Service.objects.all()[2]	# third content

	services = Service.objects.all()

	agents = Agent.objects.all()

	stars = Rating.objects.all()

	star = Rating.objects.all()[1]


	print(star)



	stars_num = range(0, 5)

	context = {'profiles': profiles, 'services': services, 'stars_num': stars_num, 'agents': agents,
				'stars': stars,}

	return render(request, 'main/index.html', context)


