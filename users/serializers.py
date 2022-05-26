from rest_framework import serializers


class UserSerializer(serializers.Serializer):

    user_id = serializers.CharField(read_only=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    first_name = serializers.charField(required=True)
    last_name = serializers.charField(required=True)
    age = serializers.IntegerField(required=True)
    cpf = serializers.CharField(required=True, min_length=11, max_length=11)
    phone = serializers.charField(required=True, min_length=15, max_length=15)
    is_staff = serializers.BooleanField(required=True)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
