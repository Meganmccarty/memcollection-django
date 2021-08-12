from rest_framework import serializers
from specimens.models import *

class SpecimenRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecimenRecord
        fields = (
            'id',
            'usi'
        )