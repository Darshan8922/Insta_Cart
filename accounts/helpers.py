from django.core.mail import send_mail
import uuid
from django.conf import settings
from decouple import config

def send_forget_password_mail(email, token):
    subject = "Your forget password Link"
    message = f"Hi, click on the link to reset your password {config('REACT_LOCAL_URL')}change-password/{token}/"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True