from rest_framework import serializers
from specimens.models import *

class SpecimenRecordSerializer(serializers.ModelSerializer):
    order = serializers.StringRelatedField(source='order.name')
    family = serializers.StringRelatedField(source='family.name')
    subfamily = serializers.StringRelatedField(source='subfamily.name')
    tribe = serializers.StringRelatedField(source='tribe.name')
    genus = serializers.StringRelatedField(source='genus.name')
    species = serializers.StringRelatedField(source='species.name')
    subspecies = serializers.StringRelatedField(source='subspecies.name')

    determiner = serializers.StringRelatedField(source='determiner.__str__')
    preparer = serializers.StringRelatedField(source='preparer.__str__')
    collector = serializers.StringRelatedField(many=True)

    country = serializers.StringRelatedField(source='country.name')
    state = serializers.StringRelatedField(source='state.name')
    county = serializers.StringRelatedField(source='county.name')
    locality = serializers.StringRelatedField(source='locality.name')
    latitude = serializers.StringRelatedField(source='gps.normalize_latitude')
    longitude = serializers.StringRelatedField(source='gps.normalize_longitude')
    elevation = serializers.StringRelatedField(source='gps.elevation_and_meters')

    class Meta:
        model = SpecimenRecord
        fields = (
            'id',
            'usi',
            'order',
            'family',
            'subfamily',
            'tribe',
            'genus',
            'species',
            'subspecies',
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
            'latitude',
            'longitude',
            'elevation',
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