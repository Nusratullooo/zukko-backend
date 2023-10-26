# Generated by Django 3.2.9 on 2023-10-19 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0035_auto_20231018_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_type',
            field=models.CharField(choices=[('Wire cover', 'Wirecover'), ('Soft cover', 'Softcover'), ('Hard cover', 'Hardcover')], default='Wire cover', max_length=100),
        ),
    ]
