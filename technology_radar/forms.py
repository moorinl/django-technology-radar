from django import forms
from django.utils.translation import ugettext as _


class SearchForm(forms.Form):
    q = forms.CharField(label=_('keywords'), max_length=128)
