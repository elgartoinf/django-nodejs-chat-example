import time
import redis

redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

from config import celery_app


@celery_app.task(bind=True)
def send_message_to_chat(self,  message):
    redis_client.publish("message", message)
