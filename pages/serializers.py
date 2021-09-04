from serpy import Serializer, IntField, StrField, Field
from images.serializers import InsectImageSerializer, PlantImageSerializer, HabitatImageSerializer
from taxonomy.serializers import SpeciesSerializer

class ReferencesSerializer(Serializer):
    id = IntField()
    title = StrField()
    citation = StrField()

class SpeciesPageSerializer(Serializer):
    id = IntField()
    title = StrField()
    get_binomial = Field(call=True)
    species = SpeciesSerializer(required=True)
    insect_images = InsectImageSerializer(many=True, attr="insect_images.all", call=True, required=False)
    plant_images = PlantImageSerializer(many=True, attr="plant_images.all", call=True, required=False)
    habitat_images = HabitatImageSerializer(many=True, attr="habitat_images.all", call=True, required=False)
    taxonomy = StrField()
    description = StrField()
    distribution = StrField()
    seasonality = StrField()
    habitat = StrField()
    food = StrField()
    life_cycle = StrField()
    display_refs = Field(call=True)
    references = ReferencesSerializer(many=True, attr="species_page.all", call=True, required=False)