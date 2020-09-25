from django.db import models



# Create your models here.
class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    real_name = models.CharField(max_length=60)
    tz = models.CharField(max_length=256, blank=True)
    activity_periods = models.ManyToManyField("UserActivity", blank=True, related_name="activity_periods")

    def __str__(self):
        return self.real_name


class UserActivity(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

