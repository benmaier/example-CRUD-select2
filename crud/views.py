from django.shortcuts import render
from django import forms
from django.views.generic.edit import UpdateView, CreateView

# Create your views here.

from django_select2.forms import ModelSelect2MultipleWidget, ModelSelect2Widget

from .models import Geoname, Institution, Geotype

class SingleSelectWidget(ModelSelect2Widget):
    def filter_queryset(self, request, term, queryset, **dependent_fields):
        qs = super().filter_queryset(request, term, queryset, **dependent_fields)
        if not self.ordering:
            return qs
        return qs.order_by(*self.ordering)

class MultipleSelectWidget(ModelSelect2MultipleWidget):
    def filter_queryset(self, request, term, queryset, **dependent_fields):
        qs = super().filter_queryset(request, term, queryset, **dependent_fields)
        if not self.ordering:
            return qs
        return qs.order_by(*self.ordering)

class SingleGeonameSelectWidget(SingleSelectWidget):
    search_fields = ['name__icontains']
    ordering = ['-population']

class SingleGeotypeSelectWidget(SingleSelectWidget):
    search_fields = ['name__icontains']
    ordering = []

class MultipleGeonameSelectWidget(MultipleSelectWidget):
    search_fields = ['name__icontains']
    ordering = ['-population']

class GeonameCreateForm(forms.ModelForm):

    geotype = forms.ModelChoiceField(widget=SingleGeotypeSelectWidget,queryset=Geotype.objects.all())
    class Meta:
        model = Geoname
        fields = ['name','population','geotype']

class InstitutionCreateForm(forms.ModelForm):

    city = forms.ModelChoiceField(widget=SingleGeonameSelectWidget,queryset=Geoname.objects.all()) 
    responsible_for_places = forms.ModelMultipleChoiceField(widget=MultipleGeonameSelectWidget,queryset=Geoname.objects.all()) 
    class Meta:
        model = Institution
        fields = ['name','city','responsible_for_places']

class InstitutionUpdateView(UpdateView):
    model = Institution
    form_class = InstitutionCreateForm
    template_name = 'crud/default_form.html'
    success_url = "/institution/create"

class GeonameUpdateView(UpdateView):
    model = Geoname
    form_class = GeonameCreateForm
    template_name = 'crud/default_form.html'
    success_url = "/geoname/create"

class InstitutionCreateView(CreateView):
    model = Institution
    form_class = InstitutionCreateForm
    template_name = 'crud/default_form.html'
    success_url = "/institution/create"

class GeonameCreateView(CreateView):
    model = Geoname
    form_class = GeonameCreateForm
    template_name = 'crud/default_form.html'
    success_url = "/geoname/create"
