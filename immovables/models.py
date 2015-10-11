from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.shared.models import TimestampsModel, NameTimestampsModel, OrderedModel, IsEnabledModel
from core.shared.fields import PositiveDecimalField
from filebrowser.fields import FileBrowseField
from colorful.fields import RGBColorField
from subway.models import Station


class District(NameTimestampsModel, OrderedModel, IsEnabledModel):
    class Meta(OrderedModel.Meta):
        verbose_name = _('district')
        verbose_name_plural = _('districts')

    def get_absolute_url(self):
        return reverse('district-detail', kwargs={'id': self.id})


class Developer(NameTimestampsModel, IsEnabledModel):
    class Meta:
        verbose_name = _('developer')
        verbose_name_plural = _('developers')

    def get_absolute_url(self):
        return reverse('developer-detail', kwargs={'id': self.id})


class HousingEstate(NameTimestampsModel, IsEnabledModel):
    class Meta:
        verbose_name = _('housing estate')
        verbose_name_plural = _('housing estates')

    def get_absolute_url(self):
        return reverse('building-detail', kwargs={'id': self.id})

    cover_photo = FileBrowseField(verbose_name=_('cover photo'), directory='housing_estates/cover_photos/', extensions=['.jpg', '.png', '.jpeg'], max_length=500, blank=True, null=True)

    district = models.ForeignKey(to=District, verbose_name=_('district'), blank=True, null=True)
    subway_station = models.ForeignKey(to=Station, verbose_name=_('subway station'), blank=True, null=True)
    address = models.TextField(verbose_name=_('address'))

    developer = models.ForeignKey(to=Developer, verbose_name=_('developer'), blank=True, null=True)

    deadline = models.PositiveIntegerField(verbose_name=_('deadline'), blank=True, null=True)
    is_delivered = models.BooleanField(verbose_name=_('is delivered'), default=False)


class HousingEstateAdditionalPhoto(TimestampsModel, IsEnabledModel):
    class Meta:
        verbose_name = _('housing estate additional photo')
        verbose_name_plural = _('housing estate additional photos')

    housing_estate = models.ForeignKey(to=HousingEstate, verbose_name=_('housing estate'), related_name='additional_photos')
    photo = FileBrowseField(verbose_name=_('photo'), directory='housing_estates/additional_photos/', extensions=['.jpg', '.png', '.jpeg'], max_length=500, blank=True, null=True)


class FlatType(NameTimestampsModel, IsEnabledModel):
    class Meta:
        verbose_name = _('flat type')
        verbose_name_plural = _('flat types')


class FinishingType(NameTimestampsModel, IsEnabledModel):
    class Meta:
        verbose_name = _('finishing type')
        verbose_name_plural = _('finishing types')


class Assignation(TimestampsModel, IsEnabledModel):
    class Meta:
        verbose_name = _('assignation')
        verbose_name_plural = _('assignations')

    def get_absolute_url(self):
        return reverse('flat-detail', kwargs={'id': self.id})

    cover_photo = FileBrowseField(verbose_name=_('cover photo'), directory='assignations/cover_photos/', extensions=['.jpg', '.png', '.jpeg'], max_length=500, blank=True, null=True)

    housing_estate = models.ForeignKey(to=HousingEstate, verbose_name=_('housing estate'), blank=True, null=True)
    flat_type = models.ForeignKey(to=FlatType, verbose_name=_('flat type'))

    total_area = PositiveDecimalField(verbose_name=_('total area'), decimal_places=2, max_digits=10)
    living_area = PositiveDecimalField(verbose_name=_('living area'), decimal_places=2, max_digits=10, blank=True, null=True)
    kitchen_area = PositiveDecimalField(verbose_name=_('kitchen area'), decimal_places=2, max_digits=10, blank=True, null=True)

    floor = models.PositiveIntegerField(verbose_name=_('floor'), blank=True, null=True)
    floors_total = models.PositiveIntegerField(verbose_name=_('floors total'), blank=True, null=True)
    elevator_available = models.BooleanField(verbose_name=_('elevator available'), default=True)

    finishing_type = models.ForeignKey(to=FinishingType, verbose_name=_('finishing type'), blank=True, null=True)

    price = models.PositiveIntegerField(verbose_name=_('price'), blank=True, null=True)
    your_commission = models.PositiveIntegerField(verbose_name=_('your commission'), blank=True, null=True)

    def __str__(self):
        return self.housing_estate.name


class AssignationAdditionalPhoto(TimestampsModel, IsEnabledModel):
    class Meta:
        verbose_name = _('assignation additional photo')
        verbose_name_plural = _('assignation additional photos')

    assignation = models.ForeignKey(to=Assignation, verbose_name=_('assignation'), related_name='additional_photos')
    photo = FileBrowseField(verbose_name=_('photo'), directory='assignations/additional_photos/', extensions=['.jpg', '.png', '.jpeg'], max_length=500, blank=True, null=True)
