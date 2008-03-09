# Create your views here.

from django.shortcuts import get_object_or_404
from mako_django import render_to_response
from models import Page

def edit_page (request):
  '''Looks for the page that matches the request's 
     path and displays it'''
  path='/'.join(request.path.split('/')[1:])
  try:
    p=Page.objects.get(name=path)
  except:
    p=None
  return render_to_response('editor.html',{ 'page': p})

def view_page (request):
  '''Looks for the page that matches the request's 
     path and displays it'''
  path=request.path
  get_object_or_404(Page,name=request.path)
  return render_to_response('viewer.html',{ 'page': p})
