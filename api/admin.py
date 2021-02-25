from django.contrib import admin
from .models import Article
# Register your models here.

# admin.site.register(Article)


# customize registerd model
@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title', 'description')