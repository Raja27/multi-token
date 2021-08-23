from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from rest_framework.authentication import TokenAuthentication
import binascii
import os


class MultiToken(models.Model):
    """
    The default authorization token model.
    """

    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='custom_auth_token',
        on_delete=models.CASCADE, verbose_name=_("User")
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        # Work around for a bug in Django:
        # https://code.djangoproject.com/ticket/19422
        #
        # Also see corresponding ticket:
        # https://github.com/tomchristie/django-rest-framework/issues/705
        # abstract = 'rest_framework.authtoken' not in settings.INSTALLED_APPS
        verbose_name = _("Multi Token")
        verbose_name_plural = _("Multi Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(MultiToken, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key


class MultiTokenAuthentication(TokenAuthentication):

    model = MultiToken

