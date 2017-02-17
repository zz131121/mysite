﻿#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from backend.models import UploadFile
from PIL import Image
from moviepy.editor import *
import datetime
import os

def index(req):
  novel_list=UploadFile.objects.filter(typ="novel")
  novel_name=[]
  for novel in novel_list:
    novel_name.append(novel.name+'.'+novel.exname)
  pic_list=UploadFile.objects.filter(typ="image")
  pic_name=[]
  for pic in pic_list:
    pic_name.append(pic.timestamp+'.'+pic.exname)
  movie_list=UploadFile.objects.filter(typ="movie")
  movie_name=[]
  for movie in movie_list:
    movie_name.append(movie.timestamp+'.'+movie.exname)
  return render(req, 'backend.html',{'pic_list':pic_name,'novel_list':novel_name,'movie_list':movie_name})

def upload(req):
  domain_name=req.REQUEST.get('domain','xxx')
  if domain_name == 'homepage':
    if req.method == 'POST':
      content = req.FILES['ContextField']#picfile要和html里面一致
    if len(UploadFile.objects.filter(timestamp='00000000000000')):
      a = UploadFile.objects.get(timestamp='00000000000000')
      try:
        os.remove('upload/'+a.name+'.'+a.exname)
      except:
        pass
    else:
      a = UploadFile()
      a.timestamp='00000000000000'
    fn = content.name
    a.name = content.name.split('.')[0]
    a.exname = content.name.split('.')[-1]
    a.save()
    if not os.path.exists('upload'):     #路径不存在时创建一个
      os.makedirs('upload')
    f_path='upload/'+fn
    with open(f_path, 'wb+') as info:  
      for chunk in content.chunks(): 
        info.write(chunk)
  else:
    if req.method == 'POST':
      content = req.FILES.getlist('ContextField')#picfile要和html里面一致
    for f in content:
      a=UploadFile()
      fnex = f.name.split('.')[-1]
      fn = ''
      tsp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
      fn = tsp
      n = 1;
      while 1:
        if len(UploadFile.objects.filter(timestamp=fn)):
          fn = tsp+'_'+str(n)
          n = n+1
        else:
          break
      a.timestamp = fn
      fn+='.'
      fn+=fnex
      if not os.path.exists('upload'):     #路径不存在时创建一个
        os.makedirs('upload')
      f_path='upload/'+fn
      with open(f_path, 'wb+') as info:  
        for chunk in f.chunks(): 
          info.write(chunk)
      if domain_name=='image':
        imagecache = Image.open(f)
        imagecache.thumbnail((250,250),Image.ANTIALIAS)
        imagecache.convert('RGB').save('upload/'+'cache_'+fn,"jpeg")
      if domain_name=='movie':
        clip = VideoFileClip('upload/'+fn)
        clip.save_frame('upload/'+'mp4t_'+a.timestamp+'.jpeg',t=1.00)
        imagecache = Image.open('upload/'+'mp4t_'+a.timestamp+'.jpeg')
        imagecache.thumbnail((250,250),Image.ANTIALIAS)
        imagecache.convert('RGB').save('upload/'+'mp4_'+a.timestamp+'.jpeg',"jpeg")
      a.exname = fnex
      a.name = f.name.split('.')[0].encode('utf-8')
      a.typ = domain_name
      a.save()
  return HttpResponseRedirect('backend')
  
def delete(req):
  domain_name=req.REQUEST.get('domain','xxx')
  file_name=req.REQUEST.get('title','xxx')
  b = UploadFile.objects.get(timestamp=file_name.split('.')[0], exname=file_name.split('.')[1])
  b.delete()
  os.remove('upload/'+b.timestamp+'.'+b.exname)
  if domain_name=='image':
    try:
      os.remove('upload/'+'cache_'+b.timestamp+'.jpeg')
    except:
      pass
  if domain_name=='movie':
    try:
      os.remove('upload/'+'mp4t_'+b.timestamp+'.jpeg')
      os.remove('upload/'+'mp4_'+b.timestamp+'.jpeg')
    except:
      pass
  return HttpResponseRedirect('backend')
 
# Create your views here.