from rest_framework import serializers
from .models import Person, Curse

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        read_only_fields = ('id',)
        
class CurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curse
        fields = "__all__"
        read_only_fields = ('id', "dateCreate", "dateUpdate")