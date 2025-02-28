from django.db import models
from django.contrib.auth.models import User

class URL(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    custom_alias = models.CharField(max_length=100, null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.long_url
