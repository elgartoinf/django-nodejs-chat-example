from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from chat_node_example.chat.api import ChatApi
from chat_node_example.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("chat", ChatApi)


app_name = "api"
urlpatterns = router.urls
