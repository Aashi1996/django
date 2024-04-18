from django.shortcuts import render

# Create your views here.
def full_diamond(request):
    output1=""
    if request.method=="POST":
        s1=(request.POST.get("input1"))
        len1=len(s1)
        s2=" "
        for j in range(0,len1-5,1):   
            for i in range(0,len1-j,1):
                output1=output1+s2
            output1=output1+s1[0:(1+(2*j))]
            output1+="\n"


        for j in range(len1-7,-1,-1):   
            for i in range(0,len1-j,1):
                output1=output1+s2
            output1=output1+s1[0:(1+(2*j))]
            output1+="\n"
    return render(request,"full_diamond.html",{"message1":output1})
