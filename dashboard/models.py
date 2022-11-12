from django.db import models

# Create your models here.
class DailyNav(models.Model):
    snapshot_date = models.DateField(null = True, verbose_name = "Nav Snapshot Date")
    total_expected_shareclass = models.IntegerField(null=True, verbose_name = "Total Expected Number Of Shareclass")
    pending_shareclass = models.IntegerField(null=True, verbose_name = "Total Pending Number Of Shareclass")
    record_insert_datetime =  models.DateTimeField(null = True, verbose_name = "Record Inserted Date and Time")
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.id}'
 
    class Meta:
        verbose_name_plural = "Backlog Daily Navs"