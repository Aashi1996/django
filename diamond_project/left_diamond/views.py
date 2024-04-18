from django.shortcuts import render

# Create your views here.
def left_diamond(request):
    output1=""
    if request.method=="POST":
        s1=(request.POST.get("input1"))
        len1=len(s1)
        s2=" "

        for j in range(1,len1+1,1):   
            for i in range(0,len1-j,1):
                output1=output1+s2
            
            output1=output1+s1[0:j]
            output1+="\n"

        for j in range(1,len1,1):   
            for i in range(0,j,1):
                output1=output1+s2
            output1=output1+s1[0:len1-j]
            output1+="\n"
    return render(request,"left_diamond.html",{"message1":output1})
