from rest_framework import serializers
from specimens.models import *

class SpecimenRecordSerializer(serializers.ModelSerializer):
    determiner = serializers.StringRelatedField(source='determiner.__str__')
    preparer = serializers.StringRelatedField(source='preparer.__str__')
    collector = serializers.StringRelatedField(many=True)
    class Meta:
        model = SpecimenRecord
        fields = (
            'id',
            'usi',
            'taxon',
            'authority',
            'common_name',
            'mona',
            'p3',
            'determiner',
            'determined_year',
            'sex',
            'stage',
            'preparer',
            'preparation',
            'preparation_date',
            'labels_printed',
            'labeled',
            'photographed',
            'identified',
            'collecting_trip',
            'country',
            'state',
            'county',
            'locality',
            'gps',
            'collected_date',
            'full_date',
            'display_collectors',
            'collector',
            'method',
            'weather',
            'temp_F',
            'temp_C',
            'time_of_day',
            'habitat',
            'notes'
        )