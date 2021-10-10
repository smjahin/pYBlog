from django.contrib import admin
from blog.models import Post, Category, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author')
    list_filter = ('author',)
    prepopulated_fields = {'title_tag':('title',)}

admin.site.register(Post, PostAdmin) 
admin.site.register(Category)
admin.site.register(Comment)