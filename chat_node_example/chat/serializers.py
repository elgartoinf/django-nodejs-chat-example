# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.fields import ReadOnlyField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from chat_node_example.chat.models import Chat


class ChatSerializer(ModelSerializer):
    author_full_name = SerializerMethodField()

    def get_author_full_name(self, object):
        return "{}: ({})".format(object.author.username, object.author.get_full_name())

    class Meta:
        model = Chat
        fields = ("date","message","room","author", "author_full_name")
        read_only_fields = ("author_full_name", "author", "date")
