from django.shortcuts import render
def home(request):
    s1="EAT"
    list1=[]
    c1=s1[0:1]
    c2=s1[1:2]
    c3=s1[2:3]
    list1.append(c1+c2+c3)
    list1.append(c1+c3+c2)
    list1.append(c2+c1+c3)
    list1.append(c2+c3+c1)
    list1.append(c3+c1+c2)
    list1.append(c3+c2+c1)
    return render(request,'app1/index.html',{'param1':list1})