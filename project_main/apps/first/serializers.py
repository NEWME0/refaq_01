from rest_framework.serializers import Serializer, CharField


class FirstSerializer(Serializer):
    one_field = CharField()
    two_field = CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
