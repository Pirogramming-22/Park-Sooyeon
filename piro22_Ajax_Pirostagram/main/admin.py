from django.contrib import admin
from . import models

@admin.register(models.Post)
class CustomPostAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class CustomCommentAdmin(admin.ModelAdmin):
    pass