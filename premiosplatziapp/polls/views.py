from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('HELLO Wordl')

def detail(request,question_id):
    return HttpResponse('detalle')

def results(request,question_id):
    return HttpResponse('result')

def vote(request,question_id):
    return HttpResponse('vote')

# Create your views here.
