from django.contrib import admin
from blog.models import Article
from blog.models import Category
from blog.models import Tag

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
