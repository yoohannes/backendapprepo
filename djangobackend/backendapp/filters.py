from dataclasses import field
import django_filters

from .models import *


class TesterFilter(django_filters.FilterSet):
    class Meta:
        model = Pics
        exclude = ["video_file"]
        fields = ["tester__tester_ID", "tester__test_id"]
