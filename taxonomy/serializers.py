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
        fields = ('id', 'order', 'name', 'common_name', 'authority', 'subfamilies')

class SubfamilySerializer(serializers.ModelSerializer):
    family = serializers.CharField(source='family.name')
    tribes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Subfamily
        fields = ('id', 'family', 'name', 'common_name', 'authority', 'tribes')

class TribeSerializer(serializers.ModelSerializer):
    subfamily = serializers.CharField(source='subfamily.name')
    genera = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tribe
        fields = ('id', 'subfamily', 'name', 'common_name', 'authority', 'genera')

class GenusSerializer(serializers.ModelSerializer):
    tribe = serializers.CharField(source='tribe.name')
    species = serializers.StringRelatedField(many=True)

    class Meta:
        model = Genus
        fields = ('id', 'tribe', 'name', 'common_name', 'authority', 'species')

class SpeciesSerializer(serializers.ModelSerializer):
    genus = serializers.CharField(source='genus.name')
    subspecies = serializers.StringRelatedField(many=True)

    class Meta:
        model = Species
        fields = ('id', 'genus', 'name', 'common_name', 'authority', 'mona', 'p3', 'subspecies')

class SubspeciesSerializer(serializers.ModelSerializer):
    species = serializers.CharField(source='species.name')

    class Meta:
        model = Subspecies
        fields = ('id', 'species', 'name', 'common_name', 'authority', 'mona', 'p3')