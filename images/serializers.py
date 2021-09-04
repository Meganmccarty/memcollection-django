from serpy import Serializer, IntField, StrField, BoolField, Field
from geography.serializers import *
from taxonomy.serializers import SpeciesSerializer

class InsectImageSerializer(Serializer):
    id = IntField()
    get_image_url = Field(call=True)
    name = StrField()
    caption = StrField()
    alt_text = StrField()
    date = StrField()
    other_notes = StrField()

    species = SpeciesSerializer(required=True)
    identified = BoolField()
    sex = StrField()
    stage = StrField()
    status = StrField()

    country = CountrySerializer(required=False)
    state = StateSerializer(required=False)
    county = CountySerializer(required=False)
    locality = LocalitySerializer(required=False)
    gps = GPSSerializer(required=False)
    collecting_trip = CollectingTripSerializer(required=False)

class PlantImageSerializer(Serializer):
    id = IntField()
    get_image_url = Field(call=True)
    name = StrField()
    caption = StrField()
    alt_text = StrField()
    date = StrField()
    other_notes = StrField()

    latin_name = StrField()
    common_name = StrField()

    country = CountrySerializer(required=False)
    state = StateSerializer(required=False)
    county = CountySerializer(required=False)
    locality = LocalitySerializer(required=False)
    gps = GPSSerializer(required=False)
    collecting_trip = CollectingTripSerializer(required=False)

class HabitatImageSerializer(Serializer):
    id = IntField()
    get_image_url = Field(call=True)
    name = StrField()
    caption = StrField()
    alt_text = StrField()
    date = StrField()
    other_notes = StrField()

    country = CountrySerializer(required=False)
    state = StateSerializer(required=False)
    county = CountySerializer(required=False)
    locality = LocalitySerializer(required=False)
    gps = GPSSerializer(required=False)
    collecting_trip = CollectingTripSerializer(required=False)