from rest_framework import serializers
from taxonomy.models import *

class SubspeciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subspecies
        fields = ('id', 'name', 'common_name', 'authority', 'mona', 'p3')

class SpeciesSerializer(serializers.ModelSerializer):
    subspecies = SubspeciesSerializer(many=True)

    class Meta:
        model = Species
        fields = ('id', 'name', 'common_name', 'authority', 'mona', 'p3', 'subspecies')

class GenusSerializer(serializers.ModelSerializer):
    species = SpeciesSerializer(many=True)

    class Meta:
        model = Genus
        fields = ('id', 'name', 'common_name', 'authority', 'species')

class TribeSerializer(serializers.ModelSerializer):
    genera = GenusSerializer(many=True)

    class Meta:
        model = Tribe
        fields = ('id', 'name', 'common_name', 'authority', 'genera')

class SubfamilySerializer(serializers.ModelSerializer):
    tribes = TribeSerializer(many=True)

    class Meta:
        model = Subfamily
        fields = ('id', 'name', 'common_name', 'authority', 'tribes')

class FamilySerializer(serializers.ModelSerializer):
    subfamilies = SubfamilySerializer(many=True)

    class Meta:
        model = Family
        fields = ('id', 'name', 'common_name', 'authority', 'subfamilies')

class OrderSerializer(serializers.ModelSerializer):
    families = FamilySerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'name', 'common_name', 'authority', 'families')