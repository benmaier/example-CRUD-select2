from django.urls import path
from .views import InstitutionUpdateView, InstitutionCreateView, GeonameUpdateView, GeonameCreateView

urlpatterns = [
    path('institution/update/<int:pk>', InstitutionUpdateView.as_view()),
    path('institution/create/', InstitutionCreateView.as_view()),
    path('geoname/update/<int:pk>', GeonameUpdateView.as_view()),
    path('geoname/create/', GeonameCreateView.as_view()),
]
