from django.db import models

class CallTrends(models.Model):     
    class Meta:
        db_table = 'tblCallTrends'

    time = models.CharField(name = "Time", max_length=100)
    calls = models.IntegerField(name = "Calls")
    abnd = models.IntegerField(name = "Abnd")

    def __str__(self):
        return self.Time