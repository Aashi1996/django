from django.db import models

# Create your models here.
class photocopy(models.Model):
    item_name=models.CharField(max_length=30)
    item_quantity=models.IntegerField(default=0)
    item_price=models.IntegerField(default=0)
    item_total=models.IntegerField(default=0)
