from django.db import models

class Weapons(models.Model):
    weapon_name = models.CharField(max_length=100, primary_key=True)
    min_damage = models.PositiveSmallIntegerField()
    max_damage = models.PositiveSmallIntegerField()
    ignore_armour = models.DecimalField(max_digits = 5, decimal_places= 2)
    eff_armour = models.DecimalField(max_digits = 5, decimal_places= 2)
    fatigue = models.PositiveSmallIntegerField()

