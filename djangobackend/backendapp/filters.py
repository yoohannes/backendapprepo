from dataclasses import field
import django_filters

from .models import Tester

class TesterFilter(django_filters.FilterSet):
    class Meta:
        model=Tester
        exclude = ['video_file']
        fields='__all__'