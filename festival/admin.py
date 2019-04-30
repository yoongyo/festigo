from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Festival, Comment, Region, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']


class FestivalAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', )


class CommentAdmin(admin.ModelAdmin):
    list_display = ['festival', 'author']


admin.site.register(Region, RegionAdmin)
admin.site.register(Festival, FestivalAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
