from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from num2words import num2words
from gtts import gTTS
from playsound import playsound


# Create your views here.
def index(request):
    return render(request, 'index.html')


def numToWord(request):

    if request.POST["num"]:
        num = (request.POST["num"])
        if num.isnumeric():
            if int(num) > 0 and int(num) <= 1000000:
                res = num2words(int(num), lang="en").title()

                return render(request, 'result.html', {'num': num, 'result': res, 'play': play})

    return redirect('/')


def play(request):

    if request.POST["num"]:
        num = (request.POST["num"])
        if num.isnumeric():
            if int(num) > 0 and int(num) <= 1000000:
                res = num2words(int(num), lang="en").title()
                myobj = gTTS(text=res, lang='en', slow=False)
                myobj.save("welcome.mp3")
                playsound("welcome.mp3")

    return redirect('/')
