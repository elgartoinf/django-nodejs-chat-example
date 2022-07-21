from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE, ForeignKey
from django.db.models.fields import TextField, DateTimeField

User = get_user_model()

class Room(models.Model):
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.pk)

class Chat(models.Model):
    date = DateTimeField(auto_now_add=True)
    message = TextField()
    room = ForeignKey(
        Room,
        on_delete=CASCADE,
        related_name="room"
    )
    author = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="author"
    )

    def __str__(self):
        return "{} {}".format(self.author, self.message)
