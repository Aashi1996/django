from django import forms
from django.shortcuts import render

# Create your views here.

class NameForm(forms.Form):
    player1 = forms.CharField(label="Player 1 ")
    player2 = forms.CharField(label="Player 2 ")

class WordForm(forms.Form):
    word1 = forms.CharField
    word2 = forms.CharField

def index(request):
    return render(request, "word/index.html", {
        "form": NameForm()
        })

def play(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return render(request, "word/play.html", {
        "form": WordForm()
        })
        else:
            return render(request, "word/index.html", {
                "form": form
                })



