from rest_framework import serializers
from tracker.models import Object, Person


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ('person_id', 'date', 'x', 'y', 'z')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'number')