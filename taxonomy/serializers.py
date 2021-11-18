from django.db.models import Max
import random
from images.models import InsectImage
from serpy import Serializer, IntField, StrField, FloatField, MethodField

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
    image = StrField()
    alt_text = StrField()
    # image = MethodField()

    # def get_image(self, family_obj):
    #     images = InsectImage.objects.filter(species__genus__tribe__subfamily__family__name=family_obj.name)
    #     if images:
    #         max_pk = images.aggregate(max_pk=Max('pk'))['max_pk']
    #         object = images.filter(pk=random.randint(1, max_pk)).first()
    #         if object:
    #             return {
    #                 'name': object.name,
    #                 'url': object.get_image_url(),
    #                 'alt_text': object.alt_text
    #             }

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