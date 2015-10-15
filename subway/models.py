from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.shared.models import TimestampsModel, NameTimestampsModel, OrderedModel, IsEnabledModel
from colorful.fields import RGBColorField
from django.core.exceptions import ValidationError


class Branch(NameTimestampsModel, OrderedModel, IsEnabledModel):
    class Meta(OrderedModel.Meta):
        verbose_name = _('subway branch')
        verbose_name_plural = _('subway branches')

    def get_absolute_url(self):
        return reverse('subway-branch-detail', kwargs={'id': self.id})

    color = RGBColorField(colors=('#FF0000', '#0070BB', '#009245', '#FBA820',
                                  '#662C91'), verbose_name=_('color'))


class Station(NameTimestampsModel, OrderedModel, IsEnabledModel):

    class Meta(OrderedModel.Meta):
        verbose_name = _('subway station')
        verbose_name_plural = _('subway stations')
        order_with_respect_to = 'branch'
        # TODO: provide a manager with an alphabetical ordering shortcut

    def get_absolute_url(self):
        return reverse('subway-station-detail', kwargs={'id': self.id})

    branch = models.ForeignKey(to=Branch, verbose_name=_('branch'))


class Interchange(TimestampsModel):

    class Meta:
        verbose_name = _('interchange')
        verbose_name_plural = _('interchanges')

    def get_absolute_url(self):
        return reverse('interchange-detail', kwargs={'id': self.id})

    from_station = models.ForeignKey(to=Station, verbose_name=_('from station'), related_name='interchanges')
    to_station = models.ForeignKey(to=Station, verbose_name=_('to station'), related_name='+')
    unique_together = ('from_station', 'to_station')
    index_together = ('from_station', 'to_station')

    def __str__(self):
        return "%s => %s" % (self.from_station, self.to_station)

    def save(self, commit=True):
        if self.from_station == self.to_station:
            raise ValidationError('from and to stations must differ')
        if commit:
            # keep relation symmetry
            super(Interchange, self).save(commit)
            try:
                Interchange.objects.get(from_station=self.to_station, to_station=self.from_station)
            except Interchange.DoesNotExist:
                reflection = Interchange()
                reflection.from_station = self.to_station
                reflection.to_station = self.from_station
                reflection.save()
            return self
        else:
            super(Interchange, self).save(commit)
            return self
