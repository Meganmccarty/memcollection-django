from rest_framework import serializers
from pages.models import SpeciesPage

class SpeciesPageSerializer(serializers.ModelSerializer):
    references = serializers.StringRelatedField(many=True)

    class Meta:
        model = SpeciesPage
        fields = (
            'get_binomial',
            'taxonomy',
            'description',
            'distribution',
            'seasonality',
            'habitat',
            'food',
            'life_cycle',
            'display_refs',
            'references'
        )