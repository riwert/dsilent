from django.contrib import admin
from .models import Post, PostAdmin, PostImage, Category, CategoryAdmin, Tag, Setting

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(PostImage)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Setting)
