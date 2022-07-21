from django.apps import AppConfig


class ChatConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "chat_node_example.chat"

    def ready(self):
        import chat_node_example.chat.signals
