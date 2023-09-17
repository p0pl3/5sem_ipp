from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=127)
    phone = models.CharField(max_length=12)

