from django.db import models

class Weapons(models.Model):
    weapon_name = models.CharField(max_length=100)
    min_damage = models.PositiveSmallIntegerField()
    max_damage = models.PositiveSmallIntegerField()
    ignore_armour = models.DecimalField()
    eff_armour = models.DecimalField()
    fatigue = models.PositiveSmallIntegerField()

