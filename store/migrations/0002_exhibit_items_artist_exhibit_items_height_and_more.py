# Generated by Django 4.1 on 2022-09-16 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibit_items',
            name='artist',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='exhibit_items',
            name='height',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='exhibit_items',
            name='summary',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='exhibit_items',
            name='width',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
