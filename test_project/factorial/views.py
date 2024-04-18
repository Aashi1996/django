from django.shortcuts import render

# Create your views here.
def factorial(request):
    num=1
    fact=1

    for i in range(1,num+1):
        fact=fact*i
    return render(request,"factorial.html",{"message1":num,"message2":fact})
