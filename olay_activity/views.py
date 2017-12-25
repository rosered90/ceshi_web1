# -*- coding: utf-8 -*-
import time
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def olay_list(request):
	"""
	:param request:
	:return:
	"""
	return render_to_response('olay_activity/index.html', locals(), context_instance=RequestContext(request))


def activity_olay1(request):
	"""
	:param request:
	:return:
	"""
	return render_to_response('olay_activity/activity_olay1.html', locals(), context_instance=RequestContext(request))


def olay_index(request):
	"""
	:param request:
	:return:
	"""
	return render_to_response('olay_activity/Olay_index.html', locals(), context_instance=RequestContext(request))
