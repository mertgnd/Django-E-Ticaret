# Generated by Django 2.2.12 on 2020-11-28 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='state',
        ),
        migrations.RemoveField(
            model_name='order',
            name='zipcode',
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=28, verbose_name='Şehir'),
        ),
    ]
