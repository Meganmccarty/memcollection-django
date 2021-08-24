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