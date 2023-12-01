from django.contrib import admin
from .models import Comment
# Register your models here.

# post/admin.py

admin.site.register(Comment)
from .models import Post, Category, Tag, Rule

admin.site.register(Post)
admin.site.register(Rule)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Tag, TagAdmin)

