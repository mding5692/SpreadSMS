from rest_framework import serializers
from tracker.models import *


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ('person_id', 'date', 'x', 'y', 'z')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'number')


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name', 'country', 'city')