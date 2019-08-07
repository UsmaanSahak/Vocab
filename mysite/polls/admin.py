# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import ReviewCard
from .models import NewCard
from .models import OldCard
admin.site.register(ReviewCard)
admin.site.register(NewCard)
admin.site.register(OldCard)


