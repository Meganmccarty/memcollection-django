from serpy import Serializer, IntField, StrField, FloatField, Field

class GPSSerializer(Serializer):
    id = IntField()
    latitude = FloatField(required=False)
    longitude = FloatField(required=False)
    elevation = StrField()

class LocalitySerializer(Serializer):
    id = IntField()
    name = StrField()
    range_and_town = Field(call=True, required=False)
    # places_collected = GPSSerializer(many=True, attr="places_collected.all", call=True, required=False)

class CountySerializer(Serializer):
    id = IntField()
    name = StrField()

class StateSerializer(Serializer):
    id = IntField()
    name = StrField()
    abbr = StrField()

class CountrySerializer(Serializer):
    id = IntField()
    name = StrField()
    abbr = StrField()

class CollectingTripSerializer(Serializer):
    id = IntField()
    name = StrField()
    states = StateSerializer(many=True, attr="states.all", call=True)
    start_date = StrField()
    end_date = StrField()
    notes = StrField()