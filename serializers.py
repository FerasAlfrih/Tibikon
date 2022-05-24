from django.db.models import fields
from rest_framework import serializers
from .models import *


class SaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saints
        fields = "__all__"
