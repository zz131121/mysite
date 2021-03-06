from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import template
from PIL import Image
from backend.models import UploadFile
import os
import os.path

def index(req):
  class picn(object):
    def __init__(self, ori, cache):
      self.ori = ori
      self.cache = cache
  tit=req.REQUEST.get('title','xxx')
  if(tit=='xxx'): 
    pic_list=UploadFile.objects.filter(typ="image")
    pic_name = []
    for pic in reversed(pic_list):
      pname=pic.timestamp+'.'+pic.exname
      chche_name='cache_'+pname
      pic_name.append(picn(pname,chche_name))
    return render(req, 'image_index.html',{'pic_list':pic_name})
  else:
    pic = UploadFile.objects.get(timestamp=tit.split('.')[0])
    pic_name = pic.timestamp+'.'+pic.exname
    return render(req, 'image.html',{'pic':pic_name})

# Create your views here.
