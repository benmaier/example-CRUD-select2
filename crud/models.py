from django.db import models

class Geotype(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Geoname(models.Model):
    name = models.CharField(max_length=255)
    population = models.PositiveIntegerField(blank=True,null=True)
    geotype = models.ForeignKey(Geotype,models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(Geoname,models.SET_NULL,blank=True,null=True)
    responsible_for_places = models.ManyToManyField(Geoname,blank=True,related_name='responsible_institutions')

    def __str__(self):
        return self.name

