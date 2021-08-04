from django.db import models
from twitteruser_app.models import TwitterUser
from tweet_app.models import Tweet
from django.utils import timezone


class Notification(models.Model):
    receiver = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name="receiver")
    msg_content = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

# Create your models here.
