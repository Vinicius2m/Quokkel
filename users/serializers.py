from rest_framework import serializers


class AdminSerializer(serializers.Serializer):

    user_id = serializers.UUIDField(read_only=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    cpf = serializers.CharField(required=True, min_length=11, max_length=11)
    phone = serializers.CharField(required=True, min_length=11, max_length=13)
    is_staff = serializers.BooleanField(required=True)


class GuestsSerializer(serializers.Serializer):

    user_id = serializers.UUIDField(read_only=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    cpf = serializers.CharField(required=True, min_length=11, max_length=11)
    phone = serializers.CharField(required=True, min_length=11, max_length=13)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
