# Generated by Django 3.2.9 on 2022-03-16 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0006_transaction_is_canceled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('verified', 'verified'), ('paid', 'paid'), ('canceled', 'canceled')], default='new', max_length=10),
        ),
    ]
