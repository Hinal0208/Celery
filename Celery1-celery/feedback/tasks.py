from time import sleep
from django.core.mail import send_mail
from celery import shared_task
import sys


@shared_task()
def send_feedback_email_task(email_address, message):
    """Sends an email when the feedback form has been submitted."""
    sleep(5) # Simulate expensive operation(s) that freeze Django
    for i in range(10):
        send_mail(
            "Your Feedback",
            f"\t{message}\n\nThank you!",
            "support@example.com",
            [email_address],
            fail_silently=False,
        )

# def send_emails():
#     recipitents=['hinal.panchal82582@gmail.com']
#     subject = 'celery'
#     message='hello'

#     for recipitent in recipitents:

    
    
    