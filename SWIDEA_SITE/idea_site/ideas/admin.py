from django.contrib import admin
from .models import Idea

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'interest', 'is_starred', 'devtool') 
    list_filter = ('is_starred', 'devtool')
    search_fields = ('title', 'content') 
    ordering = ('-id',)
