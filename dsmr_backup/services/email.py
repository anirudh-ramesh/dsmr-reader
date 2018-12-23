import logging

from django.core.mail.backends.smtp import EmailBackend
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.core import mail

from dsmr_backup.models.settings import EmailSettings
from dsmr_backend.models.settings import BackendSettings


logger = logging.getLogger('commands')


def send_backup():
    backend_settings = BackendSettings.get_solo()
    email_settings = EmailSettings.get_solo()

    logger.debug(
        ' - Email backup: Preparing to send email using mail server %s:%s',
        email_settings.host,
        email_settings.port
    )
    email_backend = EmailBackend(
        host=email_settings.host,
        port=email_settings.port,
        username=email_settings.username,
        password=email_settings.password,
        use_tls=email_settings.use_tls,
        use_ssl=email_settings.use_ssl
    )

    # Force translations.
    with translation.override(language=backend_settings.language):
        logger.debug(' - Email backup: Sending email to %s', email_settings.email_to)
        mail.EmailMessage(
            _('DSMR-reader day/hour statistics backup'),
            _('This is an automated email, containing a backup of the day and hour statistics in the attachment.'),
            email_settings.email_to,
            [email_settings.email_to],
            connection=email_backend,
        ).send()
