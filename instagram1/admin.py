from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Comment, Tag


# Register your models here.

# admin.site.register(Post)

# class PostAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(Post, PostAdmin)

# Wrapping
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'photo_tag', 'massage', 'massage_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['massage']
    list_filter = ['created_at', 'is_public']
    search_fields = ['massage']
    # form = PostForm

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f"<img src='{post.photo.url}' style='width: 72px; height: 72px;'/>")
        return None

    def massage_length(self, post):
        return f"{len(post.massage)} 글자"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass