from django.contrib import admin

from elastt_app.models import Article, Category

# Register your models here.

admin.site.register(Category)
admin.site.register(Article)