from rest_framework import serializers
from images.models import InsectImage, PlantImage, HabitatImage

class InsectImageSerializer(serializers.ModelSerializer):
    genus = serializers.StringRelatedField(source='species.genus.name')
    species = serializers.StringRelatedField(source='species.name')
    species_page = serializers.StringRelatedField()

    country = serializers.StringRelatedField(source='country.name')
    state = serializers.StringRelatedField(source='state.name')
    county = serializers.StringRelatedField(source='county.name')
    locality = serializers.StringRelatedField(source='locality.name')
    gps_lat = serializers.StringRelatedField(source='gps.latitude')
    gps_long = serializers.StringRelatedField(source='gps.longitude')
    collecting_trip = serializers.StringRelatedField(source='collecting_trip.name')

    class Meta:
        model = InsectImage
        fields = (
            'id',
            'image',
            'name',
            'caption',
            'alt_text',
            'datetime',
            'other_notes',
            'genus',
            'species',
            'species_page',
            'identified',
            'sex',
            'stage',
            'status',
            'country',
            'state',
            'county',
            'locality',
            'gps_lat',
            'gps_long',
            'collecting_trip'
        )

class PlantImageSerializer(serializers.ModelSerializer):
    species_page = serializers.StringRelatedField(many=True)

    country = serializers.StringRelatedField(source='country.name')
    state = serializers.StringRelatedField(source='state.name')
    county = serializers.StringRelatedField(source='county.name')
    locality = serializers.StringRelatedField(source='locality.name')
    gps_lat = serializers.StringRelatedField(source='gps.latitude')
    gps_long = serializers.StringRelatedField(source='gps.longitude')
    collecting_trip = serializers.StringRelatedField(source='collecting_trip.name')

    class Meta:
        model = PlantImage
        fields = (
            'id',
            'image',
            'name',
            'caption',
            'alt_text',
            'datetime',
            'other_notes',
            'latin_name'
            'common_name',
            'species_page',
            'country',
            'state',
            'county',
            'locality',
            'gps_lat',
            'gps_long',
            'collecting_trip'
        )

class HabitatImageSerializer(serializers.ModelSerializer):
    species_page = serializers.StringRelatedField(many=True)

    country = serializers.StringRelatedField(source='country.name')
    state = serializers.StringRelatedField(source='state.name')
    county = serializers.StringRelatedField(source='county.name')
    locality = serializers.StringRelatedField(source='locality.name')
    gps_lat = serializers.StringRelatedField(source='gps.latitude')
    gps_long = serializers.StringRelatedField(source='gps.longitude')
    collecting_trip = serializers.StringRelatedField(source='collecting_trip.name')

    class Meta:
        model = PlantImage
        fields = (
            'id',
            'image',
            'name',
            'caption',
            'alt_text',
            'datetime',
            'other_notes',
            'species_page',
            'country',
            'state',
            'county',
            'locality',
            'gps_lat',
            'gps_long',
            'collecting_trip'
        )