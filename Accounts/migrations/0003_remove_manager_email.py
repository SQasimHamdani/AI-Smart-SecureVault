# Generated by Django 3.0.6 on 2021-05-18 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_auto_20210519_0225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='email',
        ),
    ]
