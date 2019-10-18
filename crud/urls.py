from django.urls import path
from .views import InstitutionUpdateView, InstitutionCreateView, GeonameUpdateView, GeonameCreateView

urlpatterns = [
        path('institution/update/', InstitutionUpdateView.as_view()),
    path('institution/create/', InstitutionCreateView.as_view()),
    path('geoname/update/', GeonameUpdateView.as_view()),
    path('geoname/create/', GeonameCreateView.as_view()),
]
