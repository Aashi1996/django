# Generated by Django 4.0.3 on 2022-03-28 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_photocopy_item_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='photocopy',
            name='item_total',
            field=models.IntegerField(default=0),
        ),
    ]
