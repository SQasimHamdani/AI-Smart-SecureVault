# Generated by Django 3.0.6 on 2021-05-19 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_remove_manager_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='address',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='manager',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='ManagersLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logged_in_at', models.DateTimeField(auto_now=True)),
                ('user_profile', models.ManyToManyField(to='Accounts.Manager')),
            ],
        ),
    ]