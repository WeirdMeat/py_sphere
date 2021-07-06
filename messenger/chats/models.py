from django.db import models
from blogs.models import User


class Chat(models.Model):
    title = models.CharField(max_length=30)
    users = models.ManyToManyField(
        User,
    )

    def __str__(self):
        return self.title


class Message(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE
    )
    content = models.TextField()
    write_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['write_time']

# Create your models here.
