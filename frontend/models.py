from django.db import models
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from django.urls import reverse
from ckeditor.fields import RichTextField


class Contact(models.Model):
    full_name = models.CharField(_('Full Name'), max_length=100)
    email = models.EmailField(_('Email'), max_length=200)
    topics = models.CharField(_('Topics'), max_length=250)
    message = models.TextField(_('Message'))

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    slug = AutoSlugField(populate_from="name", unique=True)
    feature_image = models.ImageField(
        blank=True, null=True, upload_to='frontend/blog/categories/%Y/%m/%d/', default='default-thumb.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Blog (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    feature_image = ImageField(_('Feature Image'), blank=True, null=True,
                               upload_to='frontend/blog/articles/%Y/%m/%d/', default='default-thumb.png')
    title = models.CharField(_('Title'), max_length=300)
    slug = AutoSlugField(populate_from="title", unique_with='published__month')
    published = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, related_name='category')
    content = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug})


class Page(models.Model):
    title = models.CharField(_('Title'), max_length=300)
    slug = AutoSlugField(populate_from="title", unique=True)
    content = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
