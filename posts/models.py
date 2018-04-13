from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.contrib import admin

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True, max_length=255, default=None, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class CategoryAdmin(admin.ModelAdmin):
    def _get_unique_slug(self, obj):
        slug = slugify(obj.name)
        unique_slug = slug
        num = 1
        while Category.objects.exclude(id=obj.id).filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = self._get_unique_slug(obj)
        super().save_model(request, obj, form, change)

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.name = slugify(self.name)
        super().save()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(unique=True, max_length=255, default=None, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class PostAdmin(admin.ModelAdmin):
    def _get_unique_slug(self, obj):
        slug = slugify(obj.title)
        unique_slug = slug
        num = 1
        while Post.objects.exclude(id=obj.id).filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        if not obj.slug:
            obj.slug = self._get_unique_slug(obj)
        super().save_model(request, obj, form, change)
