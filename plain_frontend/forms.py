from django import forms
from immovables.models import FlatType, FinishingType, District, Developer, HousingEstate
from subway.models import Station, Branch
from django.utils.translation import ugettext_lazy as _

class AssignationFilterForm(forms.Form):
    subway_branch = forms.ModelChoiceField(label=_('subway branch'), queryset=Branch.objects.enabled(), required=False)
    subway_station = forms.ModelChoiceField(label=_('subway station'), queryset=Station.objects.enabled(), required=False)
    district = forms.ModelChoiceField(label=_('district'), queryset=District.objects.enabled(), required=False)

    developer = forms.ModelChoiceField(label=_('developer'), queryset=Developer.objects.enabled(), required=False)
    housing_estate = forms.ModelChoiceField(label=_('housing estate'), queryset=HousingEstate.objects.enabled(), required=False)
    flat_type = forms.ModelChoiceField(label=_('flat type'), queryset=FlatType.objects.enabled(), required=False)

    finishing_type = forms.ModelChoiceField(label=_('finishing type'), queryset=FinishingType.objects.enabled(), required=False)
