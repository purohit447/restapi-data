from django.db import models

# Create your models here.
class data(models.Model):
    user_id = models.IntegerField()
    mov1 = models.IntegerField()
    mov2 = models.IntegerField()
    mov3 = models.IntegerField()
    mov4 = models.IntegerField()
    mov5 = models.IntegerField()
    totalWatchTime = models.FloatField()
    weeklyWatchTime = models.FloatField()
    rewardPoints = models.IntegerField()

    def __str__(self):
        return str(self.user_id)