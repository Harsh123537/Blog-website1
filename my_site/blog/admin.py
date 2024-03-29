from django.contrib import admin
from .models import Author, Post, Tag,Comment
 
class PostAdmin(admin.ModelAdmin):
    list_filter=('date',"tag","author",)
    list_display=('date',"title","author",)
    prepopulated_fields={"slug":("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display=('user_name','post')

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)


