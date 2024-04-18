from django.shortcuts import render
from shop.models import photocopy
# Create your views here.
def db(request):
    name=photocopy.objects.all()
    quantity=photocopy.objects.all()
    price=photocopy.objects.all()
    total=photocopy.objects.all()
    message1={
        "item_name":name
        }
    message2={
        "item_quantity":quantity
        }
    message3={
        "item_price":price
        }
    return render(request,"db.html",message1,message2,message3)
