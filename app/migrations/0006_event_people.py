# Generated by Django 3.2.7 on 2022-04-19 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_event_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='people',
            field=models.IntegerField(null=True),
        ),
    ]
