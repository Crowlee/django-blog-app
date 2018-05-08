from django.contrib import admin
from .models import Post
# Register your models here.

class Postadmin(admin.ModelAdmin):
    list_display = ['id','title','count_text']
    list_display_links = ['title']

    def count_text(self,post):
        return '{}글자'.format(len(post.text))
admin.site.register(Post,Postadmin)