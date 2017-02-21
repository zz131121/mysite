from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import template
from backend.models import UploadFile
import os
import os.path

def index(req):
  class movien(object):
    def __init__(self, ori, cache):
      self.ori = ori
      self.cache = cache
  tit=req.REQUEST.get('title','xxx')
  if(tit=='xxx'): 
    movie_list=UploadFile.objects.filter(typ="movie")
    movie_name = []
    for movie in reversed(movie_list):
      pname=movie.timestamp+'.'+movie.exname
      chche_name='mp4_'+movie.timestamp+'.jpeg'
      movie_name.append(movien(pname,chche_name))
    return render(req, 'movie_index.html',{'movie_list':movie_name})
  else:
    movie = UploadFile.objects.get(timestamp=tit.split('.')[0])
    pname=movie.timestamp+'.'+movie.exname
    chche_name='mp4t_'+movie.timestamp+'.jpeg'
    movie_name = movien(pname,chche_name)
    return render(req, 'movie.html',{'movie':movie_name})

# Create your views here.
