from django.db import models

# Create your models here.
class concatenation_points(models.Model):
    con_type = models.CharField(max_length=20)
    con_name = models.CharField(max_length=20)
    con_points = models.FloatField()

    def __str__(self):
        return self.con_type

class distance_multiplier(models.Model):
    distance = models.FloatField()
    multiplier = models.FloatField()

    def __str__(self):
        return str(self.distance)