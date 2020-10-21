from rest_framework.serializers import Serializer, CharField


class UserSerializer(Serializer):
    username = CharField()
    password = CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
