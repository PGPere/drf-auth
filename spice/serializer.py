from rest_framework import serializers
from .models import Spice


class SpiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at', 'updated_at')
        model = Spice
