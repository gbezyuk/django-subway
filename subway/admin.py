from django.contrib import admin
from .models import Branch, Station, Interchange
from django.utils.translation import ugettext_lazy as _
from core.shared.admin import OrderedModelAdmin

# for grappelli translation
_('Subway')

def colored_name_helper(station):
    return '<div style="background-color: %(color)s; color: #fff; padding: 1em; font-weight: bold;">%(name)s</div>' % {
        'color': station.branch.color if station.branch else '',
        'name': station.name
    }


class InterchangeInline(admin.StackedInline):
    model = Interchange
    fk_name = 'from_station'


class SubwayBranchAdmin(OrderedModelAdmin):
    list_display = ('id', '__str__', 'move_up_down_links', 'name', 'color', 'is_enabled')
    list_display_links = ('id', '__str__')
    list_editable = ('name', 'color', 'is_enabled')

admin.site.register(Branch, SubwayBranchAdmin)


class SubwayStationAdmin(OrderedModelAdmin):
    list_display = ('id', 'colored_name', 'move_up_down_links', 'name', 'branch', 'is_enabled', 'created', 'modified', 'order', '_order')
    list_display_links = ('id', 'colored_name',)
    list_editable = ('name', 'is_enabled', 'branch')
    list_filter = ('branch', 'is_enabled')

    def colored_name(self, obj):
        return colored_name_helper(obj)
    colored_name.allow_tags = True
    colored_name.short_description = _('station')

    inlines = (InterchangeInline,)

admin.site.register(Station, SubwayStationAdmin)


class InterchangeAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_colored_name', 'to_colored_name', 'created', 'modified')

    def from_colored_name(self, obj):
        return colored_name_helper(obj.from_station)
    from_colored_name.allow_tags = True
    from_colored_name.short_description = _('from station')
    def to_colored_name(self, obj):
        return colored_name_helper(obj.to_station)
    to_colored_name.allow_tags = True
    to_colored_name.short_description = _('to station')

admin.site.register(Interchange, InterchangeAdmin)
