from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {
            'password': {
                # this will only to be post and not returned as a read field
                'write_only': True,
                'min_length': 5
            }
        }

    def create(self, validated_data):
        '''Create and return a user with encrypted password'''
        return get_user_model().objects.create_user(**validated_data)
