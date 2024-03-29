from rest_framework import serializers
from.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'email', 'name', 'year_of_study', 'prn']
