# Generated by Django 3.2.7 on 2022-04-06 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200, null=True)),
                ('theme', models.CharField(max_length=200, null=True)),
                ('people', models.IntegerField()),
                ('location', models.CharField(max_length=200, null=True)),
                ('select_date', models.DateTimeField()),
            ],
        ),
    ]
