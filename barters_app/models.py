from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from datetime import timedelta
from django.utils import timezone

QUANTITY_UNIT_CHOICES = [
    ('CT', 'count'),
    ('LB', 'pound'),
    ('CY', 'cubic yard'),
]

class Barter(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='barters')

    title = models.CharField(_('title'), max_length=255, blank=False, default=None)
    description = models.CharField(_('description'), max_length=1000)

    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)
    date_expires = models.DateTimeField(_('expires on'))

    quantity = models.DecimalField(_('quantity'), decimal_places=2, max_digits=10, default=1.0)
    quantity_units = models.CharField(_('units'), choices=QUANTITY_UNIT_CHOICES, default='CT', max_length=2)
    will_trade_for = models.CharField(_('will trade for'), max_length=255)
    is_free = models.BooleanField(_('free'), default=False)

    postal_code = models.CharField(_('postal code'), max_length=12)
    latitude = models.CharField(_('latitude'), max_length=10, null=True, blank=True)
    longitude = models.CharField(_('longitude'), max_length=10, null=True, blank=True)
    cross_street_1 = models.CharField(_('cross street 1'), max_length=255, null=True, blank=True)
    cross_street_2 = models.CharField(_('cross street 2'), max_length=255, null=True, blank=True)


    def save(self, *args, **kwargs):

        if not self.date_expires:
            self.date_expires = timezone.now() + timedelta(days=7)
            
        if not self.title:
            raise ValueError('Title cannot be blank')

        if not self.is_free and not self.will_trade_for:
            raise ValueError("Unless an item is free it must be traded for something. Check that the item's is_free value is False.")
        
        if not self.postal_code:
            raise ValueError("Please provide postal code.")

        super(Barter, self).save(*args, **kwargs)


class SeedBarter(Barter):
    genus = models.CharField(_('genus'), max_length=255, null=True, blank=True)
    species = models.CharField(_('species'), max_length=255, null=True, blank=True)
    common_name = models.CharField(_('common_name'), max_length=255, null=True, blank=True)
    year_packaged = models.PositiveIntegerField(_('date_packaged'), null=True)


class PlantBarter(Barter):
    genus = models.CharField(_('genus'), max_length=255, null=True, blank=True)
    species = models.CharField(_('species'), max_length=255, null=True, blank=True)
    common_name = models.CharField(_('common_name'), max_length=255, null=True, blank=True)
    date_planted = models.DateField(max_length=255, null=True, blank=True)


class ProduceBarter(PlantBarter):
    date_harvested = models.DateField(null=True)


class MaterialBarter(Barter):
    pass

class ToolBarter(Barter):
    dimensions = models.CharField(_('dimensions'), help_text='Height x Width x Length', max_length=64, null=True, blank=True)