# Create your tasks here

from celery import shared_task
from django.core.cache import cache
from django.core.mail import send_mail


@shared_task
def check_users():
    file = open('application/users.txt', 'a')
    file.write(str(cache.get('users_in_system', 0)) + '\n')
    file.close()


@shared_task
def send_email():
    send_mail(
        subject='new_object',
        message='new object created',
        from_email='spheredjango@gmail.com',
        recipient_list=['chundraman@gmail.com'],
        fail_silently=False,
    )
