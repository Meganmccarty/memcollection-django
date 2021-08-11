from rest_framework import serializers
from geography.models import *

class GPSSerializer(serializers.ModelSerializer):
    locality = serializers.CharField(source='locality.name')

    class Meta:
        model = GPS
        fields = ('id', 'locality', 'latitude', 'longitude', 'elevation')

class LocalitySerializer(serializers.ModelSerializer):
    places_collected = GPSSerializer(many=True)
    
    class Meta:
        model = Locality
        fields = ('id', 'name', 'range_and_town', 'places_collected')

class CountySerializer(serializers.ModelSerializer):
    localities = LocalitySerializer(many=True)

    class Meta:
        model = County
        fields = ('id', 'name', 'localities')

class StateSerializer(serializers.ModelSerializer):
    counties = CountySerializer(many=True)
    localities = LocalitySerializer(many=True)

    class Meta:
        model = State
        fields = ('id', 'name', 'abbr', 'counties', 'localities')

class CountrySerializer(serializers.ModelSerializer):
    states = StateSerializer(many=True)
    localities = LocalitySerializer(many=True)

    class Meta:
        model = Country
        fields = ('id', 'name', 'abbr', 'states', 'localities')

class CollectingTripSerializer(serializers.ModelSerializer):
    states = serializers.StringRelatedField(many=True)

    class Meta:
        model = CollectingTrip
        fields = ('id', 'name', 'states', 'start_date', 'end_date', 'notes')