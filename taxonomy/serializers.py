from rest_framework import serializers
from taxonomy.models import *

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class FamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = Family
        fields = '__all__'

class SubfamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subfamily
        fields = '__all__'

class TribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tribe
        fields = '__all__'

class GenusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genus
        fields = '__all__'

class SpeciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Species
        fields = '__all__'

class SubspeciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subspecies
        fields = '__all__'