# Generated by Django 2.2.12 on 2020-11-29 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_odeme2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='odeme2',
        ),
    ]
