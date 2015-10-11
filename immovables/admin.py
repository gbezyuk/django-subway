from django.contrib import admin
from .models import District, Developer, Assignation, HousingEstate, FlatType
from core.shared.admin import TimestampsAdmin, NameTimestampsAdmin, OrderedModelAdmin
from django.utils.translation import ugettext_lazy as _

# fro grappelli translation
_('Immovables')

admin.site.register(District, NameTimestampsAdmin)
admin.site.register(Developer, NameTimestampsAdmin)
admin.site.register(FlatType, NameTimestampsAdmin)


class HousingEstateAdmin(admin.ModelAdmin):
    pass

admin.site.register(HousingEstate, HousingEstateAdmin)


class AssignationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Assignation, AssignationAdmin)
