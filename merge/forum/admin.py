from django.contrib import admin
from .models import *
# Register your models here.


class ThreadAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Thread._meta.fields]

    class Meta:
        model = Thread

admin.site.register(Thread, ThreadAdmin)


class PostAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)