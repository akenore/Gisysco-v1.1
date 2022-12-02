# Generated by Django 3.2.16 on 2022-11-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('topics', models.CharField(max_length=250, verbose_name='Topics')),
                ('message', models.TextField(verbose_name='Message')),
            ],
        ),
    ]