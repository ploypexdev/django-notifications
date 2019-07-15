from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from celery import shared_task

@shared_task
def send_notification_email(verb, description, timesince, email):
    email = EmailMessage(
        verb,
        f'{description} happened {timesince} ago',  # render_to_string
        'New Notification <notifications@example.com>',
        [email],
        reply_to=['Support <support@example.com']
    )
    # email.content_subtype = 'html'
    email.send()
