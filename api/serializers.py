from rest_framework import serializers

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=User._meta.get_field('id'), required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'user_type')
        extra_kwargs = {
            'id': {'validators': []},
            'email': {'validators': []},
            'username': {'validators': []},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
