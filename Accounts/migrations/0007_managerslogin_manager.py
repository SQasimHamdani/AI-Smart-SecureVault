# Generated by Django 3.0.6 on 2021-05-19 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_remove_managerslogin_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='managerslogin',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.Manager'),
        ),
    ]
