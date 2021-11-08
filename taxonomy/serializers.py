from serpy import Serializer, IntField, StrField, FloatField

class SubspeciesSerializer(Serializer):
    id = IntField()
    name= StrField()
    common_name = StrField(required=False)
    authority = StrField()
    mona = FloatField(required=False)
    p3 = FloatField(required=False)

class SpeciesSerializer(Serializer):
    id = IntField()
    name= StrField()
    common_name = StrField(required=False)
    authority = StrField()
    mona = FloatField(required=False)
    p3 = FloatField(required=False)

class GenusSerializer(Serializer):
    id = IntField()
    name= StrField()
    common_name = StrField(required=False)
    authority = StrField()

class TribeSerializer(Serializer):
    id = IntField()
    name= StrField()
    common_name = StrField(required=False)
    authority = StrField()

class SubfamilySerializer(Serializer):
    id = IntField()
    name= StrField()
    common_name = StrField(required=False)
    authority = StrField()    

class FamilySerializer(Serializer):
    id = IntField()
    name= StrField()
    common_name = StrField(required=False)
    authority = StrField()

class OrderSerializer(Serializer):
    id = IntField()
    name = StrField()
    common_name = StrField(required=False)
    authority = StrField()

class NestedFamilySerializer(Serializer):
    id = IntField()
    name= StrField()
    common_name = StrField(required=False)
    authority = StrField()
    order = OrderSerializer()

class NestedSubfamilySerializer(Serializer):
    id = IntField()
    name= StrField()
    common_name = StrField(required=False)
    authority = StrField()
    family = NestedFamilySerializer()

class NestedTribeSerializer(Serializer):
    id = IntField()
    name= StrField()
    common_name = StrField(required=False)
    authority = StrField()
    subfamily = NestedSubfamilySerializer()

class NestedGenusSerializer(Serializer):
    id = IntField()
    name= StrField()
    common_name = StrField(required=False)
    authority = StrField()
    tribe = NestedTribeSerializer()

class NestedSpeciesSerializer(Serializer):
    id = IntField()
    name= StrField()
    common_name = StrField(required=False)
    authority = StrField()
    mona = FloatField(required=False)
    p3 = FloatField(required=False)
    genus = NestedGenusSerializer()
    subspecies = SubspeciesSerializer(many=True, attr="subspecies.all", call=True, required=False)