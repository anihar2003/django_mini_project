# email_sender.py

from django.core.mail import EmailMessage
from django.conf import settings

def send_test_email():
    subject = 'Test Email'
    message = 'This is a test email sent from Django.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['studymaterialdbit@gmail.com']
    
    email = EmailMessage(subject, message, email_from, recipient_list)
    email.send()
