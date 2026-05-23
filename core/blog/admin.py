from django.contrib import admin
from blog.models import Post, category

# Register your models here.

class PostAdmin(admin.ModelAdmin):

    list_display = ['author', 'title', 'status', 'created_date', 'published_date']

admin.site.register(Post,PostAdmin)
admin.site.register(category)