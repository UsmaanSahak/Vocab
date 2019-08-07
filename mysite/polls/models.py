# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ReviewCard(models.Model):
  def as_dict(self):
    return {
      "id": self.id,
      "question" : self.question,
      "answer" : self.answer,
      "date" : self.date,
      "binNum" : self.binNum,
      "correctNum" : self.binNum,
      "wrongNum" : self.wrongNum
    }

  question = models.CharField(max_length=50)
  answer = models.CharField(max_length=200)
  date = models.DateTimeField('Timeout')
  binNum = models.IntegerField(default=0)
  correctNum = models.IntegerField(default=0)
  wrongNum = models.IntegerField(default=0)

class NewCard(models.Model):
  def as_dict(self):
    return {
      "id": self.id,
      "question" : self.question,
      "answer" : self.answer,
    }
  def class_name():
    return __class__.__name__
  question = models.CharField(max_length=50)
  answer = models.CharField(max_length=200)

class OldCard(models.Model):
  def as_dict(self):
    return {
      "id": self.id,
      "question" : self.question,
      "answer" : self.answer,
      "correctNum" : self.binNum,
      "wrongNum" : self.wrongNum,
      "reason" : self.reason
    }
  question = models.CharField(max_length=50)
  answer = models.CharField(max_length=200)
  correctNum = models.IntegerField(default=0)
  wrongNum = models.IntegerField(default=0)
  reason = models.CharField(max_length=60)



