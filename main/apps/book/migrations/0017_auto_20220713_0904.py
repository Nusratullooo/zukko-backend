# Generated by Django 3.2.9 on 2022-07-13 09:04

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0016_auto_20220323_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='short_description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='short_description_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title'),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]