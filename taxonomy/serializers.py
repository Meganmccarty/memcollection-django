from rest_framework import serializers
from taxonomy.models import *

class OrderSerializer(serializers.ModelSerializer):
    families = serializers.StringRelatedField(many=True)

    class Meta:
        model = Order
        fields = ('id', 'name', 'common_name', 'authority', 'families')

class FamilySerializer(serializers.ModelSerializer):
    order = serializers.CharField(source='order.name')
    subfamilies = serializers.StringRelatedField(many=True)

    class Meta:
        model = Family
        fields = ('id', 'name', 'common_name', 'authority', 'order', 'subfamilies')

class SubfamilySerializer(serializers.ModelSerializer):
    family = serializers.CharField(source='family.name')
    tribes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Subfamily
        fields = ('id', 'name', 'common_name', 'authority', 'family', 'tribes')

class TribeSerializer(serializers.ModelSerializer):
    subfamily = serializers.CharField(source='subfamily.name')
    genera = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tribe
        fields = ('id', 'name', 'common_name', 'authority', 'subfamily', 'genera')

class GenusSerializer(serializers.ModelSerializer):
    tribe = serializers.CharField(source='tribe.name')
    species = serializers.StringRelatedField(many=True)

    class Meta:
        model = Genus
        fields = ('id', 'name', 'common_name', 'authority', 'tribe', 'species')

class SpeciesSerializer(serializers.ModelSerializer):
    genus = serializers.CharField(source='genus.name')
    subspecies = serializers.StringRelatedField(many=True)

    class Meta:
        model = Species
        fields = ('id', 'name', 'common_name', 'authority', 'mona', 'p3', 'genus', 'subspecies')

class SubspeciesSerializer(serializers.ModelSerializer):
    species = serializers.CharField(source='species.name')

    class Meta:
        model = Subspecies
        fields = ('id', 'name', 'common_name', 'authority', 'mona', 'p3', 'species')