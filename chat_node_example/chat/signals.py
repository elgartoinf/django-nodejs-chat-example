# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import post_save
from django.dispatch import receiver

from chat_node_example.chat.models import Chat
from .tasks import send_message_to_chat


@receiver(post_save, sender=Chat)
def send_message_chat(sender, instance, **kwargs):
    data = "{}".format({"date": "{}".format(instance.date), "message": instance.message, "room": "{}".format(instance.room.pk),
                                "author": "{}: ({})".format(instance.author.username, instance.author.get_full_name())})
    print(data)
    send_message_to_chat.apply_async(args=(data,))
