from serpy import Serializer, IntField, StrField, BoolField, Field
from taxonomy.serializers import *
from geography.serializers import *

class PersonSerializer(Serializer):
    id = IntField()
    first_name = StrField()
    middle_initial = StrField()
    last_name = StrField()
    suffix = StrField()

class SpecimenRecordImageSerializer(Serializer):
    id = IntField()
    get_image_url = Field(call=True)
    position = StrField()
    date = StrField()

class SpecimenRecordSerializer(Serializer):
    id = IntField()
    usi = StrField()
    images = SpecimenRecordImageSerializer(many=True, attr="specimen_images.all", call=True, required=False)
    order = OrderSerializer(required=False)
    family = FamilySerializer(required=False)
    subfamily = SubfamilySerializer(required=False)
    tribe = TribeSerializer(required=False)
    genus = GenusSerializer(required=False)
    species = SpeciesSerializer(required=False)
    subspecies = SubspeciesSerializer(required=False)
    taxon = Field(call=True)
    common_name = Field(call=True)
    authority = Field(call=True)
    mona = Field(call=True)
    p3 = Field(call=True)
    determiner = PersonSerializer(required=False)
    determined_year = IntField(required=False)
    sex = StrField()
    stage = StrField()
    preparer = PersonSerializer(required=False)
    preparation = StrField()
    preparation_date = StrField(required=False)
    labels_printed = BoolField()
    labeled = BoolField()
    photographed = BoolField()
    identified = BoolField()
    collecting_trip = CollectingTripSerializer(required=False)
    country = CountrySerializer(required=False)
    state = StateSerializer(required=False)
    county = CountySerializer(required=False)
    locality = LocalitySerializer(required=False)
    gps = GPSSerializer(required=False)
    collected_date = Field(call=True)
    full_date = Field(call=True)
    display_collectors = Field(call=True)
    collector = PersonSerializer(many=True, attr="collector.all", call=True, required=False)
    method = StrField(required=False)
    weather = StrField(required=False)
    temp_F = Field(call=True)
    temp_C = Field(call=True)
    time_of_day = StrField(required=False)
    habitat = StrField(required=False)
    notes = StrField(required=False)

# class SpecimenRecordSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     usi = serializers.CharField()
#     order = serializers.StringRelatedField(source='order.name')
#     # order_common_name = serializers.StringRelatedField(source='order.common_name')
#     # order_authority_name = serializers.StringRelatedField(source='order.common_name')
#     # order = OrderSerializer(required=False)
#     sex = serializers.CharField()
#     photographed = serializers.BooleanField()

#     class Meta:
#         model = SpecimenRecord
#         fields = ['id', 'usi', 'order', 'sex', 'photographed']
#         read_only_fields = fields

# class SpecimenRecordSerializer(serializers.ModelSerializer):
#     order = serializers.StringRelatedField(source='order.name')

#     class Meta:
#         model = SpecimenRecord
#         fields = ['id', 'usi', 'order', 'sex', 'photographed']

# class SpecimenRecordSerializer(serializers.ModelSerializer):
#     order = serializers.StringRelatedField(source='order.name')
#     family = serializers.StringRelatedField(source='family.name')
#     subfamily = serializers.StringRelatedField(source='subfamily.name')
#     tribe = serializers.StringRelatedField(source='tribe.name')
#     genus = serializers.StringRelatedField(source='genus.name')
#     species = serializers.StringRelatedField(source='species.name')
#     subspecies = serializers.StringRelatedField(source='subspecies.name')

#     determiner = serializers.StringRelatedField(source='determiner.__str__')
#     preparer = serializers.StringRelatedField(source='preparer.__str__')
#     collector = serializers.StringRelatedField(many=True)

#     collecting_trip = serializers.StringRelatedField(source='collecting_trip.name')
#     country = serializers.StringRelatedField(source='country.name')
#     state = serializers.StringRelatedField(source='state.name')
#     county = serializers.StringRelatedField(source='county.name')
#     locality = serializers.StringRelatedField(source='locality.name')
#     latitude = serializers.StringRelatedField(source='gps.normalize_latitude')
#     longitude = serializers.StringRelatedField(source='gps.normalize_longitude')
#     elevation = serializers.StringRelatedField(source='gps.elevation_and_meters')

#     class Meta:
#         model = SpecimenRecord
#         fields = (
#             'id',
#             'usi',
#             'order',
#             'family',
#             'subfamily',
#             'tribe',
#             'genus',
#             'species',
#             'subspecies',
#             # 'taxon',
#             'authority',
#             'common_name',
#             'mona',
#             'p3',
#             'determiner',
#             'determined_year',
#             'sex',
#             'stage',
#             'preparer',
#             'preparation',
#             'preparation_date',
#             'labels_printed',
#             'labeled',
#             'photographed',
#             'identified',
#             'collecting_trip',
#             'country',
#             'state',
#             'county',
#             'locality',
#             'latitude',
#             'longitude',
#             'elevation',
#             'collected_date',
#             # 'full_date',
#             'display_collectors',
#             'collector',
#             'method',
#             'weather',
#             'temp_F',
#             'temp_C',
#             'time_of_day',
#             'habitat',
#             'notes'
#         )
#         read_only_fields = fields