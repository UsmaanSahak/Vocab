# Generated by Django 2.2.4 on 2019-08-07 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20190807_0126'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewCard',
        ),
        migrations.DeleteModel(
            name='OldCard',
        ),
        migrations.AddField(
            model_name='reviewcard',
            name='seen',
            field=models.IntegerField(default=0),
        ),
    ]
