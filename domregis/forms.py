from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Domain, GroupDomain

class DomainCreate(forms.ModelForm):
    class Meta:
        # merelasikan form dengan model
        model = Domain
        # mengeset field apa saja yang akan ditampilkan pada form
        fields = ('sub_domain', 'group_domain')
        # mengatur teks label untuk setiap field
        labels = {
            'sub_domain': _('Sub Domain'),
            'group_domain': _('Group Domain')
        }
        error_messages = {
            'sub_domain': {
                'required': _("Please enter your sub-domain."),
            },
            'group_domain': {
                'required': _("Please enter your domain."),
            },
        }

class GroupDomainCreate(forms.ModelForm):
    class Meta:
        # merelasikan form dengan model
        model = GroupDomain
        # mengeset field apa saja yang akan ditampilkan pada form
        fields = ('group_domain', 'cpanel_domain')
        # mengatur teks label untuk setiap field
        labels = {
            'group_domain': _('Group Domain'),
            'cpanel_domain': _('Cpanel Link'),
        }
        error_messages = {
            'group_domain': {
                'required': _("Please enter your domain."),
            },
            'cpanel_domain': {
                'required': _("Please enter your cpanel link."),
            },
        }