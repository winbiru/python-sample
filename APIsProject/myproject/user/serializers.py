from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'date_joined']
        extra_kwargs = {
            'url': {'view_name': 'user:user-detail'},
        }


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']
        extra_kwargs = {
            'url': {'view_name': 'user:group-detail'},
        }
