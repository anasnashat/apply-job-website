import django_filters
from .models import job


class JobFilter(django_filters.FilterSet):
     discribe = django_filters.CharFilter(lookup_expr='icontains')
     titel = django_filters.CharFilter(lookup_expr='icontains')

     class Meta:
        model = job
        fields = '__all__'
        exclude= ( 'slug','owner','imege','puplish_time','salary','vacancy')