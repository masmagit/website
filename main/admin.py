from django.contrib import admin
from os import getenv as os_getenv
from .models import Content
from .forms import ContentForm

class ContentAdmin(admin.ModelAdmin):
    form = ContentForm

    class Media:
        js = (
            f'https://cdn.tiny.cloud/1/{os_getenv("TINY_KEY")}/tinymce/5/tinymce.min.js',
            '/static/main/tiny.js',
        )

# Register your models here.
admin.site.register(Content, ContentAdmin)
