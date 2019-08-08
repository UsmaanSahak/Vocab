# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
import datetime
from .models import ReviewCard
# Create your views here.


def index(request):
  if (ReviewCard.objects.count() == 0):
    context = {'q' : "null"}
    return render(request,'polls/index.html',context)
  elif (ReviewCard.objects.filter(seen=1).count() > 0 and ReviewCard.objects.filter(seen=1).order_by("date")[:1].get().date < datetime.datetime.now(datetime.timezone.utc)):
    Card = ReviewCard.objects.filter(seen=1).order_by('date')[:1].get()
    context = {
      'q' : Card,
      'type' : "ReviewCard"
    }
    return render(request,'polls/index.html', context)
  elif (ReviewCard.objects.filter(seen=0).order_by("date").count() > 0):
    Card = ReviewCard.objects.filter(seen=0).order_by('date')[:1].get()
    context = {
      'q' : Card,
      'type' : "NewCard"
    }
    return render(request,'polls/index.html', context)
  elif (ReviewCard.objects.filter(seen=1).count() > 0):
    #return render(request,'polls/index.html', {"type":"NoCard"})
    return render(request,'polls/index.html', {"q": "Temporarily"})
  else:
    return render(request,'polls/index.html', {"q": "Permanently"})

def addTime(obj):
    if (obj.binNum == 1):
      obj.date = datetime.datetime.now() + datetime.timedelta(seconds=5)
    elif (obj.binNum == 2):
      obj.date = datetime.datetime.now() + datetime.timedelta(seconds=25)
    elif (obj.binNum == 3):
      obj.date = datetime.datetime.now() + datetime.timedelta(minutes=2)
    elif (obj.binNum == 4):
      obj.date = datetime.datetime.now() + datetime.timedelta(minutes=10)
    elif (obj.binNum == 5):
      obj.date = datetime.datetime.now() + datetime.timedelta(hours=1)
    elif (obj.binNum == 6):
      obj.date = datetime.datetime.now() + datetime.timedelta(hours=5)
    elif (obj.binNum == 7):
      obj.date = datetime.datetime.now() + datetime.timedelta(days=1)
    elif (obj.binNum == 8):
      obj.date = datetime.datetime.now() + datetime.timedelta(days=5)
    elif (obj.binNum == 9):
      obj.date = datetime.datetime.now() + datetime.timedelta(days=25)
    elif (obj.binNum == 10):
      obj.date = datetime.datetime.now() + datetime.timedelta(days=120)#4 months * 30
    else:
      obj.seen = 2
    obj.save() 


    
def updateEntry(request):
  obj = ReviewCard.objects.get(id=(request.GET['id']))
  if obj.seen == 0:
    obj.seen += 1
  if (request.GET['res'] == 'true'):
    obj.binNum += 1
    obj.correctNum += 1
    addTime(obj)
  else:
    obj.binNum = 1
    obj.wrongNum += 1
    if (obj.wrongNum > 9):
      obj.seen = 2

  result = {}
  ReviewCards = ReviewCard.objects.filter(seen=1).order_by('date')
  NewCards = ReviewCard.objects.filter(seen=0).order_by('date')
  if ReviewCard.objects.order_by('date').count() == 0:
    return HttpResponse("No cards!")
  if ReviewCards.count() > 0 and ReviewCards[:1].get().date < datetime.datetime.now(datetime.timezone.utc):
    Card = ReviewCards[:1].get()
    result['id'] = Card.id
    result['question'] = Card.question
    result['answer'] = Card.answer
    result['binNum'] = Card.binNum
    result['year'] = Card.date.year
    result['month'] = Card.date.month
    result['day'] = Card.date.day
    result['hour'] = Card.date.hour
    result['minute'] = Card.date.minute
    result['second'] = Card.date.second
    result['seen'] = Card.seen
    return HttpResponse(json.dumps(result),content_type="application/json")
  elif (NewCards.count() > 0):
    Card = NewCards[:1].get()
    result['id'] = Card.id
    result['question'] = Card.question
    result['answer'] = Card.answer
    result['binNum'] = Card.binNum
    result['year'] = Card.date.year
    result['month'] = Card.date.month
    result['day'] = Card.date.day
    result['hour'] = Card.date.hour
    result['minute'] = Card.date.minute
    result['second'] = Card.date.second
    result['seen'] = Card.seen
    return HttpResponse(json.dumps(result),content_type="application/json")
 
  elif (ReviewCards.count() != 0):
    result['binNum'] = "Temporarily"
    return HttpResponse(json.dumps(result),content_type="application/json")
  else:
    result['binNum'] = "Permanently"
    return HttpResponse(json.dumps(result),content_type="application/json")



def displayCards():
    arrDict = {}
    arrDict["NewCards"] = [obj.as_dict() for obj in NewCard.objects.order_by('date')]
    arrDict["ReviewCards"] = [obj.as_dict() for obj in ReviewCards.objects.order_by('date')]
    arrDict["OldCards"] = [obj.as_dict() for obj in OldCards.objects.order_by('id')]
    return HttpResponse(json.dumps(arrDict),content_type="application/json")


