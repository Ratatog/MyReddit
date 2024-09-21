from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Group, Post, Image, Comment


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'group_photo')
    list_display_links = ('pk', 'title', 'description')
    search_fields = ('title', 'pk')
    ordering = ('pk',)
    save_on_top = True
    
    @admin.display(description='Фото')
    def group_photo(self, group):
        return mark_safe(f'<img src="{group.photo.url}", width=50>')
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'create_date', 'post_first_photo')
    list_display_links = ('pk', 'text')
    search_fields = ('pk', 'title', 'create_date', 'tags')
    ordering = ('-create_date', 'text')
    save_on_top = True
    
    @admin.display(description='Фото')
    def post_first_photo(self, post):
        try: 
            return mark_safe(f'<img src="{post.img.first().url.url}", width=50>')
        except:
            return 'None'
    
    
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'url', 'url_image')
    list_display_links = ('pk', 'url')
    search_fields = ('pk', 'url')
    ordering = ('pk',)
    save_on_top = True
    
    @admin.display(description='Картинка')
    def url_image(self, image):
        return mark_safe(f'<img src="{image.url.url}", width=50>')
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'create_date')
    list_display_links = ('pk', 'text')
    search_fields = ('pk', 'text', 'create_date')
    ordering = ('-create_date', 'text')
    save_on_top = True