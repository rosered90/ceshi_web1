from django.shortcuts import render, render_to_response


# Create your views here.
from django.template import RequestContext

def index_base(request):
	return render_to_response('authority/index.html', locals(), context_instance=RequestContext(request))

# def index(request):
# 	return render_to_response('shop/index.html', locals(), context_instance=RequestContext(request))
#
#
# def detail(request):
# 	return render_to_response('shop/detail.html', locals(), context_instance=RequestContext(request))
