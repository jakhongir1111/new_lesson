from django.contrib import admin

from apps.models import Post


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ['views', 'slug']
    # fields = []
