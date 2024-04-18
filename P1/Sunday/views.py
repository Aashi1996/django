import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    today = datetime.datetime.today()
    return render(request, "Sunday/index.html", {
        "Sunday": today.weekday() == 6
        })
