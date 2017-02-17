#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse(u'欢迎光临仙剑侠的主页!')
# Create your views here.
