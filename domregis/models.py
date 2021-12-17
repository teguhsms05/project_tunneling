from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime


today = datetime.datetime.utcnow()+datetime.timedelta(hours=7)
# Create your models here.
class Domain(models.Model): 
    # class groupDomain(models.TextChoices):
    #     struktur = 'strukturpintar.com', _('strukturpintar.com')
    #     upajiwa = 'ubs-indonesia.net', _('ubs-indonesia.net')

    # sub_domain = models.CharField(max_length=200, null=False)
    # group_domain = models.CharField(
    #     max_length=200, 
    #     choices=groupDomain.choices,
    #     default=groupDomain.struktur)
    # createdAt = models.DateTimeField(default=today)

    # class Meta:
    #     db_table = 'domain_data'
    
    sub_domain = models.CharField(
        max_length=200, null=False)
    group_domain = models.CharField(
        max_length=200)
    # group_domain = models.CharField(
    #     max_length=200, 
    #     choices=cpanel_choices,
    #     default=cpanel_choices[0])
    createdAt = models.DateTimeField(default=today)

    class Meta:
        db_table = 'domain_data'

class GroupDomain(models.Model): 
    group_domain = models.CharField(max_length=200, null=False)
    cpanel_domain = models.CharField(max_length=200, null=False)
    createdAt = models.DateTimeField(default=today)

    class Meta:
        db_table = 'domain_group'