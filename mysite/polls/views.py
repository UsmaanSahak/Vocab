# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
import datetime
from .models import ReviewCard
from .models import NewCard
# Create your views here.


def index(request):
  if (ReviewCard.objects.count() > 0):
    Card = ReviewCard.objects.order_by('date')[:1].get()
    context = {
      'q' : Card,
      'type' : "ReviewCard"
    }
    return render(request,'polls/index.html', context)
  elif (NewCard.objects.count() > 0):
    Card = NewCard.objects.order_by('id')[:1].get()
    context = {
      'q' : Card,
      'type' : "NewCard"
    }
    return render(request,'polls/index.html', context)
  else:
    context = {'q' : "null"}
    return render(request,'polls/index.html',context)


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
      obj.date = datetime.datetime.now() + datetime.timedelta(months=4)
    obj.save() 


def processCard(request):
  if (request.GET['type'] == "ReviewCard"):
    obj = ReviewCard.objects.get(id=(request.GET['id']))
    return obj

  #elif (request.GET['type'] == "NewCard"):
  temp = NewCard.objects.get(id=(request.GET['id']))
  obj = ReviewCard(question=temp.question,answer=temp.answer,date=datetime.datetime.now() + datetime.timedelta(minutes=5),correctNum=0,wrongNum=0,binNum=0)
  temp.delete()
  return obj
 
    
def updateEntry(request):
  obj = processCard(request)
  if (request.GET['res'] == 'true'):
    obj.binNum += 1
    obj.correctNum += 1
    if (obj.binNum >= 11):
      c = OldCards(question=obj.question,answer=obj.answer,correctNum=obj.correctNum,wrongNum=obj.wrongNum)
      c.save()
      obj.delete()
    else:
      addTime(obj)
  else:
    obj.binNum = 1
    obj.wrongNum += 1

  result = {}
  ReviewCards = ReviewCard.objects.order_by('date')
  NewCards = NewCard.objects.order_by('date')
  if ReviewCards.count() != 0 and ReviewCards[:1].get().date > datetime.datetime.now(datetime.timezone.utc):
    Card = ReviewCard.objects.order_by('date')[:1].get()
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
    return HttpResponse(json.dumps(result),content_type="application/json")
  elif (ReviewCards.count() == 0 and NewCards.size() != 0):
    Card = NewCards.objects.order_by('date')[:1].get()
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
    return HttpResponse(json.dumps(result),content_type="application/json")
  elif (ReviewCards.count != 0):
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


