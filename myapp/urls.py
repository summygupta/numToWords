from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('numToWord', views.numToWord, name='numToWord'),
    #path('play', views.play, name='play'),

    # path('play', views.textToSpeech, name='play')
]
