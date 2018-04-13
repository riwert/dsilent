from django.contrib import admin
from .models import Post, PostAdmin, Category, CategoryAdmin

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
