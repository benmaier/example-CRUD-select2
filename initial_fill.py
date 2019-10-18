from crud.models import Geotype, Geoname, Institution
import random

N = 350000
wordlength = 10
maxpopulation = 10000

Geotype.objects.create(name='City')
Geotype.objects.create(name='Town')
Geotype.objects.create(name='Village')

Geoname.objects_bulk_create([
                Geoname(name= ''.join(random.choice(string.ascii_lowercase) for j in range(wordlength)),
                        population = random.rand(0,maxpopulation),
                        geotype=Geotype.objects.get(pk=random.randomint(1,3)),
                        )
                for i in range(N)]

I = Institution(name='Knagengark',
                city=Geonames.objects.get(pk=1)
                responsible_for_places = [Geonames.objects.get(pk=2), Geonames.objects.get(pk=3)]
                )
I.save()

