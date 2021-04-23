from rest_framework import serializers
from . import models

class profile(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'