# Generated by Django 3.2.9 on 2022-09-28 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0009_alter_categorytype_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
    ]