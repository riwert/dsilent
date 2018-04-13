from django.contrib import admin
from .models import Post, PostAdmin, Category, CategoryAdmin, Tag

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
