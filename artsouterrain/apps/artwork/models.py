from django.db import models
from django.utils.translation import ugettext_lazy as _


class PartnerType(models.Model):
    key = models.CharField(
        verbose_name=_("Key (use for front)"),
        null=False,
        blank=False,
        max_length=100,
        unique=True
    )

    name = models.CharField(
        verbose_name=_("Name"),
        null=False,
        blank=False,
        max_length=100
    )


class Partner(models.Model):
    name = models.CharField(
        verbose_name=_("Partner Name"),
        null=False,
        blank=False,
        max_length=100
    )

    logo = models.ImageField(
        verbose_name=_("Logo"),
        null=True,
        blank=True
    )

    link = models.URLField(
        verbose_name=_("Url to partner"),
        null=True,
        blank=True,
        max_length=1024
    )

    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=True
    )

    partner_type = models.ForeignKey(
        PartnerType,
        verbose_name=_("Type"),
        on_delete=models.CASCADE
    )
