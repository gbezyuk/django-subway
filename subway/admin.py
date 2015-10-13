from django.contrib import admin
from .models import Branch, Station
from django.utils.translation import ugettext_lazy as _
from core.shared.admin import OrderedModelAdmin

# for grappelli translation
_('Subway')


class SubwayBranchAdmin(OrderedModelAdmin):
    list_display = ('id', '__str__', 'move_up_down_links', 'name', 'color', 'is_enabled')
    list_display_links = ('id', '__str__')
    list_editable = ('name', 'color', 'is_enabled')

admin.site.register(Branch, SubwayBranchAdmin)


class SubwayStationAdmin(OrderedModelAdmin):
    list_display = ('id', 'colored_name', 'move_up_down_links', 'name', 'branch', 'is_enabled')
    list_display_links = ('id', 'colored_name',)
    list_editable = ('name', 'is_enabled', 'branch')
    list_filter = ('branch', 'is_enabled')

    def colored_name(self, obj):
        return '<div style="background-color: %(color)s; color: #fff; padding: 1em; font-weight: bold;">%(name)s</div>' % {
            'color': obj.branch.color if obj.branch else '',
            'name': obj.name
        }
    colored_name.allow_tags = True
    colored_name.short_descripiton = _('name')

admin.site.register(Station, SubwayStationAdmin)
