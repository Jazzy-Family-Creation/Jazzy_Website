# Generated by Django 3.2.7 on 2022-05-06 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_requestevent_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestevent',
            name='package',
            field=models.CharField(choices=[('Basic Deposit - 137.5 USD', 'Base'), ('Premium Deposit - 187.5 USD', 'Premium'), ('Gold Deposit - 237.5 USD', 'Gold')], max_length=200, null=True),
        ),
    ]