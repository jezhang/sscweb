# Create your views here.
# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,redirect,render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

def vote(request):
	return render(request,'vote/index.html')