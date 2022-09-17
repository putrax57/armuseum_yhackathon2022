# Generated by Django 4.1 on 2022-09-17 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_exhibit_items_artist_exhibit_items_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibit_items',
            name='fungibility',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AddField(
            model_name='exhibit_items',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=20),
        ),
    ]
