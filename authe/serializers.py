from rest_framework import serializers

from django.contrib.auth.models import User


class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "password2",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "password2": {"write_only": True},
        }

    def create(self, validated_data):
        UN = validated_data.get("username")
        EM = validated_data.get("email")
        P1 = validated_data.get("password")
        P2 = validated_data.get("password2")

        if P1 == P2:
            user = User(username=UN, email=EM)
            user.set_password(P1)
            user.save()
            return user
        else:
            serializers.ValidationError({"error": "Password does not match"})
        return super().create(validated_data)
