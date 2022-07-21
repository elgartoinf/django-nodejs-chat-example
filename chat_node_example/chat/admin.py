from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from django.contrib.auth import get_user_model

from chat_node_example.chat.models import Chat, Room

User = get_user_model()

class ChatAdmin(TabularInline):
    model = Chat

@admin.register(Room)
class RoomAdmin(ModelAdmin):
    inlines = [ChatAdmin]
