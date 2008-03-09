from django.db import models
from django import newforms as forms

class Page(models.Model):
  '''Te basic page object'''
  class Admin:
    pass
  def __unicode__(self):
    return self.title
  name  = models.CharField(max_length=40)
  '''The path where this page appears'''
  title = models.CharField(max_length=80)
  '''Title of the page'''
  text  = models.TextField(max_length=3000)
  '''Some HTML that goes in it'''
  date  = models.DateField(auto_now_add=True)
  '''Date of creation'''