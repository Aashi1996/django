from django.shortcuts import render

# Create your views here.
def right_diamond(request):
    output1=""
    if request.method=="POST":
        s1=(request.POST.get("input1"))
        len1=len(s1)
        for i in range(1,len1+1,1):
            output1=output1+s1[0:i]+"\n"
            
        for i in range(1,len1,1):
            output1=output1+s1[0:len1-i]+"\n"
    return render(request,"right_diamond.html",{"message1":output1})

