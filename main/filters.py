import django_filters
from django.db.models import Q
from .models import DoctorProfile

class DocFilterBySpec(django_filters.FilterSet):
    
    SPECS = DoctorProfile.SPECS
    
    spec = django_filters.ChoiceFilter(method="my_custom_filter", choices=SPECS)
    city = django_filters.CharFilter(field_name="city")

    class Meta:
        model = DoctorProfile
        fields = ['city']

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(spec1__icontains=value) | Q(spec2__icontains=value)
        )

class DocFilterByCity(django_filters.FilterSet):
    
    city = django_filters.CharFilter(field_name="city")

    class Meta:
        model = DoctorProfile
        fields = ['city',]