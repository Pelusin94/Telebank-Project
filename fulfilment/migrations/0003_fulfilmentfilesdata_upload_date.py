# Generated by Django 2.1.15 on 2020-06-04 21:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fulfilment', '0002_fulfilmentfilesdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='fulfilmentfilesdata',
            name='upload_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
