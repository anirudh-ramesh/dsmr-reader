from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models
from solo.models import SingletonModel


class BackendSettings(SingletonModel):
    language = models.CharField(
        max_length=32,
        default='nl',
        choices=settings.LANGUAGES,
        verbose_name=_('The language used in backend processes'),
    )
