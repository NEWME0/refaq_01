from rest_framework import serializers
from .models import Record, Player


class PartialModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(PartialModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            for field_name in set(self.fields) - set(fields):
                self.fields.pop(field_name)


class PlayerSerializer(PartialModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class RecordSerializer(PartialModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
