from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','date_posted','status']
    list_filter = ['status','date_created','date_posted','author']
    search_fields = ['title','content']
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'published'
    ordering = ['status','date_posted']
    show_facets = admin.ShowFacets.ALWAYS


