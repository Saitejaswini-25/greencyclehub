import os
from django.core.mail import send_mail

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ec.settings")

send_mail(
    "Test Email",
    "This is a test email from Django.",
    os.getenv('EMAIL_HOST_USER'),
    ["recipient @gmail.com"],  # Replace with the recipient email
    fail_silently=False,
)
