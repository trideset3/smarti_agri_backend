from django.db import models
from django.contrib.gis.db import models 


class Seasons(models.Model):
    season_name = models.CharField(max_length=256, null=True, blank =True)
    season_start = models.DateField( null=True, blank =True)
    season_end = models.DateField( null=True, blank =True)
    #description = models.CharField(max_length=256, null=True, blank=True)

class Cultures(models.Model):
    culture_name = models.CharField(max_length=256, null=True, blank=True)
    sort_name = models.CharField(max_length=256, null=True, blank=True)
    eco_production = models.BooleanField(default=False, null=True, blank=True)

class Fields(models.Model):
    field_code = models.CharField(max_length=256, null=True, blank=True)
    field_name = models.CharField(max_length=256, null=True, blank=True)
    mun_name = models.CharField(max_length=256, null=True, blank=True)
    soil_type = models.CharField(max_length=256, null=True, blank=True)
    geom = models.PolygonField()
    area_ha = models.FloatField(null=True, blank=True)
    state = models.IntegerField(null=True, blank=True)
    yield_amount = models.FloatField(null=True, blank=True)
    season = models.ForeignKey(Seasons, on_delete=models.SET_NULL, null=True, blank=True)
    culture = models.ForeignKey(Cultures, on_delete=models.SET_NULL, null=True, blank=True)



# class Yields(models.Model):
#     yield_amount = models.FloatField()
#     season = models.ForeignKey(Seasons, on_delete=models.SET_NULL, null=True, blank=True)
#     field = models.ForeignKey(Fields, on_delete=models.SET_NULL, null=True, blank=True)
#     culture = models.ForeignKey(Cultures, on_delete=models.SET_NULL, null=True, blank=True)

