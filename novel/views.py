from django.shortcuts import render
from django.http import HttpResponseRedirect
from backend.models import UploadFile
import datetime
import os

def index(req):
  tit=req.REQUEST.get('title','xxx') 
  if(tit=='xxx'):
    novel_list=UploadFile.objects.filter(typ="novel")
    novel_name=[]
    for novel in novel_list:
      novel_name.append(novel.name)
    return render(req, 'novel_index.html',{'novel_list':novel_name})
  else:
    with open(os.path.join('upload/',UploadFile.objects.get(name=tit).timestamp+'.txt')) as n:
      txt = n.read()
    try:
      txt = txt.decode("utf-8")
    except:
      pass
    try:
      txt = txt.decode("utf-16")
    except:
      pass
    try:
      txt = txt.decode("gbk")
    except:
      pass
    txt = txt.replace('\r\n','<br>')
    txt = txt.replace('\n','<br>')
    return render(req, 'novel.html',{'novel':txt})
# Create your views here.
