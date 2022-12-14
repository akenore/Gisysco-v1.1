# Generated by Django 3.2.16 on 2022-11-24 15:55

import autoslug.fields
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('feature_image', models.ImageField(blank=True, default='default-thumb.png', null=True, upload_to='frontend/blog/categories/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_image', sorl.thumbnail.fields.ImageField(blank=True, default='default-thumb.png', null=True, upload_to='frontend/blog/articles/%Y/%m/%d/', verbose_name='Feature Image')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=('published__month',))),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(related_name='category', to='frontend.Category')),
            ],
        ),
    ]
