from django.db import models

class Content(models.Model):
    page = models.CharField(max_length=50, blank=True)
    param1 = models.CharField(max_length=250, blank=True)
    param2 = models.JSONField(blank=True, null=True)
    content = models.TextField(blank=True)