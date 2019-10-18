from django.shortcuts import render
from django import forms
from django.views.generic.edit import UpdateView, CreateView

# Create your views here.

from django_select2.forms import ModelSelect2MultipleWidget, ModelSelect2Widget

from .models import Geoname, Institution

class SingleSelectWidget(ModelSelect2Widget):
    def filter_queryset(self, request, term, queryset, **dependent_fields):
        qs = super().filter_queryset(request, term, queryset, **dependent_fields)
        return qs.order_by(*self.ordering)

class MultipleSelectWidget(ModelSelect2MultipleWidget):
    def filter_queryset(self, request, term, queryset, **dependent_fields):
        qs = super().filter_queryset(request, term, queryset, **dependent_fields)
        return qs.order_by(*self.ordering)

class SingleGeonameSelectWidget(SingleSelectWidget):
    search_fields = ['name__icontains']
    ordering = ['-population']

class MultipleGeonameSelectWidget(MultipleSelectWidget):
    search_fields = ['name__icontains']
    ordering = ['-population']

class GeonameCreateForm(forms.ModelForm):

    #name = forms.CharField()
    #population = forms.IntegerField(min_value=0)
    geotype = forms.ModelChoiceField(widget=SingleGeonameSelectWidget,queryset=Geoname.objects.all()) 
    class Meta:
        model = Geoname
        fields = ['name','population','geotype']

class InstitutionUpdateView(UpdateView):
    model = Institution
    fields = ['name','city','responsible_for_places']
    template_name_suffix = '_update_form'

class GeonameUpdateView(UpdateView):
    model = Geoname
    form_class = GeonameCreateForm
    template_name_suffix = '_update_form'

    def get_object(self):
        return Geoname.objects.get(pk=self.request.GET.get('pk'))

class InstitutionCreateView(CreateView):
    model = Institution
    fields = ['name','city','responsible_for_places']

class GeonameCreateView(CreateView):
    model = Geoname
    form_class = GeonameCreateForm
