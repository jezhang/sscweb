# Create your views here.
# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,redirect,render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from vote.models import *

def vote(request):
	if request.method == 'POST':
		selected = request.POST.getlist('selected')
		name = request.POST.get('name','unkonw')
		department = request.POST.get('department','unkonw')

		countsOfVote = Votes.objects.filter(department=department).filter(name=name).count()
		if countsOfVote > 0:
			# return HttpResponse("Sorry! You have already voted!")
			return render(request, 'vote/result.html',{'response':'<h2>Sorry!</h2><p>You have already voted!</p>'})

		if not len(selected) == 2:
			# return HttpResponse("Sorry! You should selected 2 items! Please <a href='/vote'>back</a>")
			return render(request, 'vote/result.html',{'response':'<h2>Sorry!</h2><p>You should selected 2 items! Please <a class="btn btn-primary btn-lg" role="button" href="/vote">back</a></p>'})

		for item in selected:
			new_vote = Votes()
			new_vote.name = name
			new_vote.department = department
			show_id = item
			show = get_object_or_404(Show, pk=show_id)
			new_vote.show = show
			new_vote.save()			
		# return HttpResponse("Thanks for your voting!")
		return render(request, 'vote/result.html',{'response':'<h2>Congratulations!</h2><p>Thanks for your voting</p>'})
	else:
		shows = Show.objects.all().order_by('-year')
		return render(request,'vote/index.html',{'shows':shows})