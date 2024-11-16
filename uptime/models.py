from django.db import models
from django.utils import timezone

class ServerUptime(models.Model):     
    class Meta:
        db_table = 'tblServerUptime'

    hostname = models.CharField(name = "HostName", max_length=50)
    hostIntIP = models.GenericIPAddressField(name = "HostIntIP")
    BootTime = models.DateTimeField(name = "BootTime", default=timezone.now)
    upTime = models.CharField(name = "UpTime", max_length=100)

    def __str__(self):
        return self.HostName