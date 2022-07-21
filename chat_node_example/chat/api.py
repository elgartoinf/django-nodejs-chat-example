# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import GenericViewSet

from chat_node_example.chat.models import Chat
from chat_node_example.chat.serializers import ChatSerializer


class ChatApi(CreateAPIView, RetrieveUpdateAPIView, ListAPIView, GenericViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return super().get_queryset().filter(room=self.request.GET.get("room",None))
