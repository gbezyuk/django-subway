from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.shared.models import NameTimestampsModel, OrderedModel, IsEnabledModel
from colorful.fields import RGBColorField


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

    def get_absolute_url(self):
        return reverse('subway-station-detail', kwargs={'id': self.id})

    branch = models.ForeignKey(to=Branch, verbose_name=_('branch'))
