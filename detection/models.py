from django.db import models


class IpLocation(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return str(self.ip) + ' : ' + str(self.location)
