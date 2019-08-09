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
      "wrongNum" : self.wrongNum,
      "seen" : self.seen
    }

  question = models.CharField(max_length=50)
  answer = models.CharField(max_length=200)
  date = models.DateTimeField(auto_now_add=True,blank=True)
  binNum = models.IntegerField(default=0)
  correctNum = models.IntegerField(default=0)
  wrongNum = models.IntegerField(default=0)
  seen = models.IntegerField(default=0)


