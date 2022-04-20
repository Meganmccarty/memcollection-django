from serpy import Serializer, IntField, StrField, Field
from images.serializers import ShortInsectImageSerializer, ShortPlantImageSerializer, ShortHabitatImageSerializer
from taxonomy.serializers import SpeciesSerializer, NestedSpeciesSerializer

class ReferencesSerializer(Serializer):
    id = IntField()
    title = StrField()
    citation = StrField()

class ShortenedSpeciesPageSerializer(Serializer):
    id = IntField()
    title = StrField()
    get_binomial = Field(call=True)
    species = SpeciesSerializer(required=True)
    family = Field(call=True)
    order = Field(call=True)
    insect_images = ShortInsectImageSerializer(many=True, attr="insect_images.all", call=True, required=False)

class SpeciesPageSerializer(Serializer):
    id = IntField()
    title = StrField()
    get_binomial = Field(call=True)
    species = NestedSpeciesSerializer(required=True)
    genus = Field(call=True)
    tribe = Field(call=True)
    subfamily = Field(call=True)
    family = Field(call=True)
    order = Field(call=True)
    insect_images = ShortInsectImageSerializer(many=True, attr="insect_images.all", call=True, required=False)
    plant_images = ShortPlantImageSerializer(many=True, attr="plant_images.all", call=True, required=False)
    habitat_images = ShortHabitatImageSerializer(many=True, attr="habitat_images.all", call=True, required=False)
    taxonomy = StrField()
    description = StrField()
    distribution = StrField()
    seasonality = StrField()
    habitat = StrField()
    food = StrField()
    life_cycle = StrField()
    display_refs = Field(call=True)
    references = ReferencesSerializer(many=True, attr="species_page.all", call=True, required=False)