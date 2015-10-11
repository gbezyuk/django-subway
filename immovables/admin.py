from django.contrib import admin
from .models import District, Developer, Assignation, HousingEstate, FlatType, FinishingType
from core.shared.admin import NameTimestampsEnabledAdmin, OrderedModelAdmin, EnableDisableAdmin
from django.utils.translation import ugettext_lazy as _
from filebrowser.settings import ADMIN_THUMBNAIL

# fro grappelli translation
_('Immovables')

admin.site.register(District, NameTimestampsEnabledAdmin)
admin.site.register(Developer, NameTimestampsEnabledAdmin)
admin.site.register(FlatType, NameTimestampsEnabledAdmin)
admin.site.register(FinishingType, NameTimestampsEnabledAdmin)


class HousingEstateAdmin(EnableDisableAdmin):
    list_display = ('id', 'cover_thumbnail', '__str__', 'name', 'developer', 'district', 'subway_station', 'deadline', 'is_delivered',)
    list_display_links = ('id', 'cover_thumbnail', '__str__')
    list_editable = ('name', 'district', 'subway_station', 'deadline', 'is_delivered',)
    list_filter = ('is_enabled', 'is_delivered', 'developer', 'district', 'subway_station')

    def cover_thumbnail(self, obj):
        if obj.cover_photo and obj.cover_photo.filetype == "Image":
            return '<img src="%(image_url)s" alt="%(alt_text)s"/>' % {
                'image_url': obj.cover_photo.version_generate(ADMIN_THUMBNAIL).url,
                'alt_text': obj.name
            }
        else:
            return "<span>%s</span>" % _('cover photo not set')
    cover_thumbnail.allow_tags = True
    cover_thumbnail.short_description = _('cover photo')


admin.site.register(HousingEstate, HousingEstateAdmin)


class AssignationAdmin(EnableDisableAdmin):
    list_display = ('id', 'cover_thumbnail', '__str__', 'housing_estate', 'flat_type', 'total_area', 'living_area', 'kitchen_area', 'floor', 'floors_total', 'elevator_available', 'finishing_type', 'price', 'your_commission')
    list_display_links = ('id', 'cover_thumbnail', '__str__')
    list_editable = ('housing_estate', 'flat_type', 'total_area', 'living_area', 'kitchen_area', 'floor', 'floors_total', 'elevator_available', 'finishing_type', 'price', 'your_commission')
    list_filter = ('is_enabled', 'housing_estate', 'flat_type', 'floor', 'floors_total', 'elevator_available', 'finishing_type',)

    def cover_thumbnail(self, obj):
        if obj.cover_photo and obj.cover_photo.filetype == "Image":
            return '<img src="%(image_url)s" alt="%(alt_text)s"/>' % {
                'image_url': obj.cover_photo.version_generate(ADMIN_THUMBNAIL).url,
                'alt_text': obj.__str__()
            }
        else:
            return "<span>%s</span>" % _('cover photo not set')
    cover_thumbnail.allow_tags = True
    cover_thumbnail.short_description = _('cover photo')

admin.site.register(Assignation, AssignationAdmin)
