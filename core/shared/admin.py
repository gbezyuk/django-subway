from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin


class TimestampsAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'created', 'modified')
    list_display_links = ('id', '__str__')


class NameTimestampsEnabledAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'name', 'is_enabled', 'created', 'modified')
    list_display_links = ('id', '__str__')
    list_editable = ('name', 'is_enabled',)
    list_filter = ('is_enabled',)


class NameSlugTimestampsAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'name', 'slug', 'created', 'modified')
    list_display_links = ('id', '__str__')
    list_editable = ('name', 'slug')
