# import time
from django.core.mail import send_mail
from django.conf import settings

def send_mail_to_client(request):
    subject = "Test Mail"
    message = "This is a test email from django server."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["ayushmittal0506@gmail.com"]

    send_mail(subject, message, from_email, recipient_list)