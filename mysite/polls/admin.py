# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import ReviewCard
class CardsAdmin(admin.ModelAdmin):
  list_filter = ("correctNum","wrongNum")
  list_display = ("question","binNum","date","correctNum", "wrongNum")
  fields = ("question","answer")
admin.site.register(ReviewCard,CardsAdmin)

