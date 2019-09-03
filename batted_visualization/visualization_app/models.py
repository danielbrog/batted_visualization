from django.db import models
import datetime

# Create your models here.
class Hit(models.Model):
    date= models.DateField()
    gamepk=models.PositiveIntegerField()
    hometeamid=models.PositiveSmallIntegerField()
    hometeamname=models.CharField(max_length=256)
    awayteamid=models.PositiveSmallIntegerField()
    awayteamname=models.CharField(max_length=256)
    parkid=models.PositiveSmallIntegerField()
    park=models.CharField(max_length=256)
    batterid=models.PositiveIntegerField()
    battername=models.CharField(max_length=256)
    batside=models.CharField(max_length=1)
    batterteamid=models.PositiveIntegerField()
    pitcherid=models.PositiveIntegerField()
    pitchername=models.CharField(max_length=256)
    pitcherteamid=models.PositiveIntegerField()
    pitchside=models.CharField(max_length=1)
    balls=models.PositiveSmallIntegerField()
    strikes=models.PositiveSmallIntegerField()
    result_type=models.CharField(max_length=256)
    pitch_type=models.CharField(max_length=2)
    pitch_speed=models.DecimalField(max_digits=10, decimal_places=7)
    zone_location_x=models.DecimalField(max_digits=10, decimal_places=7)
    zone_location_z=models.DecimalField(max_digits=10, decimal_places=7)
    launch_speed=models.DecimalField(max_digits=10, decimal_places=7)
    launch_vert_ang=models.DecimalField(max_digits=10, decimal_places=7)
    launch_horiz_ang=models.DecimalField(max_digits=10, decimal_places=7)
    landing_location_x=models.DecimalField(max_digits=10, decimal_places=7)
    landing_location_y=models.DecimalField(max_digits=10, decimal_places=7)
    hang_time=models.DecimalField(max_digits=10, decimal_places=7)

    class Meta():
        ordering = ('date',)


    def __str__(self):
        return self.date.strftime('%m/%d/%Y')+" : "+self.battername


class Batter(models.Model):
    name=models.CharField(max_length=256)
    batterid=models.PositiveIntegerField()
    batside=models.CharField(max_length=1)
    teamid=models.PositiveIntegerField()
    teamname=models.CharField(max_length=256)

    class Meta():
        ordering = ('name',)

    def __str__(self):
        return self.name + 'from team ' + self.teamname

class Pitcher(models.Model):
    name=models.CharField(max_length=256)
    pitcherid=models.PositiveIntegerField()
    pitchside=models.CharField(max_length=1)
    max_pitch_speed=models.DecimalField(max_digits=10, decimal_places=7)
    teamid=models.PositiveIntegerField()
    teamname=models.CharField(max_length=256)

    class Meta():
        ordering = ('name',)

    def __str__(self):
        return self.name + 'from team ' + self.teamname