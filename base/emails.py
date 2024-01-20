
from django.conf import settings
from django.core.mail import send_mail

def send_account_activation_email(email, email_token):
    subject = 'Tu cuenta encesitas er verificada'
    email_from = settings.EMAIL_HOST_USER
    message = f'Hola, da click en el link para activar tu cuenta http://127.0.0.1:8000/accounts/activate/{email_token}'
    
    # Envía el correo electrónico
    send_mail(subject, message, email_from, [email])