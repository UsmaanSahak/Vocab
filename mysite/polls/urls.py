from django.urls import path
from . import views

urlpatterns = [
  path('',views.index,name='index'),
  path('updateEntry',views.updateEntry, name='updateEntry'),
  path('displayCards',views.displayCards, name='displayCards')
]
