from django.db import models

class inventory(models.Model):
    name = models.CharField(max_length =100, null=False, blank=False)