from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import signals
from application.tasks import send_email


class User(AbstractUser):
    pass


def create_new(instance, signal, *args, **kwargs):
    send_email.delay()


signals.post_save.connect(create_new)


class Post(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    content = models.CharField(max_length=10000)
    write_time = models.DateTimeField(auto_now=True)
    edit_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Create your models here.
