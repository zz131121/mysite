from django.shortcuts import render
from backend.models import UploadFile
import datetime

def index(req):
  now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  if len(UploadFile.objects.filter(timestamp='00000000000000'))==1:
    a = UploadFile.objects.get(timestamp='00000000000000')
    fn = '/upload/'+a.name+'.'+a.exname
  else:
    fn = '/static/home.jpg'
  return render(req, 'home.html', {'current_date':now,'home':fn})

# Create your views here.
