from django.db import models
from django.contrib.auth.models import User

class URL(models.Model):
    long_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.long_url

# insert should give the PK back
# retrieval take short url, convert to base10 in python, select the value where that ID is