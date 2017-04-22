from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import template
from PIL import Image
from backend.models import UploadFile
import os
import os.path
import cStringIO
import pytumblr
import urllib2
import re

def get_pics(json_data):
  pic_links=[]
  posts=json_data['posts']
  for i in posts:
    for j in i['photos']:
      tmp=[]
      tmp.append(j['original_size']['url'])
      for n in j['alt_sizes']:
        if n['width']<=300:
          tmp.append(n['url'])
          break
      pic_links.append(tmp)
  return pic_links

def img_write(req,name):
  if os.path.exists(name):
    print "Already exist"
    return
  else:
    try:
      image1=urllib2.urlopen(req,timeout=10).read()
      tmpIm = cStringIO.StringIO(image1)
      fp=open(name,'wb')
      fp.write(image1)
      fp.close()
    except:
      print "fail"
      return  

def stor_pics(pic_links):
  if not os.path.exists('upload'):
    os.makedirs('upload')
  for each in pic_links:
    print u'downloading %s'%each[0]
    req=urllib2.Request(each[0])
    req_cache=urllib2.Request(each[1])
    pic_name = 'upload/'+re.findall(r"\/(tumblr_.*)",each[0])[0]
    cache_name = 'upload/'+'cache_'+re.findall(r"\/(tumblr_.*)",each[0])[0]
    img_write(req,pic_name)
    img_write(req_cache,cache_name)

client=pytumblr.TumblrRestClient(
  'RDJqBjxgZjiYku76PkENZQSUX8KHUhNAWbeD4w7PN1CMAOy2Dr',
  'SgPxMwKWSuyayD8ikgDX3TshJplccTBBcQRQtZuEAYPRdL4zUY',
  'SOj9rfwmS7mAtb03mJhzW4zwhw3ntFaBUtOb9Ak8eUdrlhG0cZ',
  '4hpZC7G7xsPGM8HV7Kq0T1BRs8TuUiPjGmBHndY5nfWkdPMxwJ'
)

def index(req):
  class picn(object):
    def __init__(self, ori, cache):
      self.ori = ori
      self.cache = cache
  tit=req.REQUEST.get('title','xxx')
  if(tit=='xxx'): 
#    pic_list=UploadFile.objects.filter(typ="image")
#    pic_name = []
#    for pic in reversed(pic_list):
#      pname=pic.timestamp+'.'+pic.exname
#      chche_name='cache_'+pname
#      pic_name.append(picn(pname,chche_name))

#tumblr code
    pic_name = []
    pic_links=[]
    for n in range(0,5):
      dashboard_list=client.dashboard(limit=50, offset=50*n, type='photo')
      pic_links=pic_links+get_pics(dashboard_list)
    for pic in pic_links:
      pic_name.append(picn(pic[0],pic[1]))
#tumblr code

    return render(req, 'image_index.html',{'pic_list':pic_name})
  else:
    pic = UploadFile.objects.get(timestamp=tit.split('.')[0])
    pic_name = pic.timestamp+'.'+pic.exname
    return render(req, 'image.html',{'pic':pic_name})

# Create your views here.
