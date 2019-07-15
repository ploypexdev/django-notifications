''' Django notifications signal file '''
# -*- coding: utf-8 -*-
from django.dispatch import Signal, receiver
from django.db.models.signals import post_save
from django.core.mail import EmailMessage

from .models import Notification

notify = Signal(providing_args=[  # pylint: disable=invalid-name
	'recipient', 'actor', 'verb', 'action_object', 'target', 'description',
	'timestamp', 'level'
])

@receiver(post_save, sender=Notification)
def send_email_notification(sender, instance, created, *args, **kwargs):
	email = EmailMessage(
		instance.verb,
		f'{instance.description} happened {instance.timesince} ago',
		'New Notification <notifications@example.com>',
		[instance.recipient.email],
		reply_to='Support <support@example.com'
	)
	email.content_subtype = 'html'
	email.send()
