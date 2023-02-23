import django_filters
from .models import Bikes, Product, Company
# from .models import Catelogue

# # class ProductFilter(django_filters.FilterSet):
# #     price = django_filters.RangeFilter()

class ProductFilter(django_filters.FilterSet):

    # part_for_bike = django_filters.ModelChoiceFilter(field_name='part_for_bike__id')
    # part_name = django_filters.CharFilter(field_name='part_for_bike__catelogue__part_name')

    part_name = django_filters.CharFilter(field_name='part_name', lookup_expr='iexact')
    
    class Meta:
        model = Product
        fields = ['part_name']

# # part_name__part_for_bike