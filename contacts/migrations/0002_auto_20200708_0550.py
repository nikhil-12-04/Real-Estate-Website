# Generated by Django 3.0.8 on 2020-07-08 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user_id',
            field=models.IntegerField(blank=True),
        ),
    ]