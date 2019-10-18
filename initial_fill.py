import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CRUD_select2.settings')

import django
django.setup()

from crud.models import Geotype, Geoname, Institution
import random
import string
#from progressbar2 import ProgressBar as PB

N = 35000
wordlength = 10
maxpopulation = 10000

Geotype.objects.create(name='City')
Geotype.objects.create(name='Town')
Geotype.objects.create(name='Village')

Geoname.objects.bulk_create([Geoname(name= ''.join(random.choice(string.ascii_lowercase) for j in range(wordlength)),
            population = random.randint(0,maxpopulation),
            geotype=Geotype.objects.get(pk=random.randint(1,3)),
            )
            for i in range(N) ])

I = Institution(name='Knagengark',
                city=Geoname.objects.get(pk=1),
                )
I.save()
I.responsible_for_places.add(Geoname.objects.get(pk=2), Geoname.objects.get(pk=3))
I.save()

