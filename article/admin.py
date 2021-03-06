from django.contrib import admin
from .models import ArticleModel,Category,TagsModel

@admin.register(ArticleModel)
class ArticleModelAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ['title',]

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass

@admin.register(TagsModel)
class TagsModelAdmin(admin.ModelAdmin):
    pass
