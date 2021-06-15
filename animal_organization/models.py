from django.db import models

class Hospital(models.Model):

    name = models.CharField(max_length=128, blank=False, null=False)
    address = models.CharField(max_length=256, blank=False, null=True)
    phone_number = models.CharField(max_length=16, blank=False, null=True)
    home_page = models.CharField(max_length=256, blank=False, null=True)

    def __str__(self):
        return self.name