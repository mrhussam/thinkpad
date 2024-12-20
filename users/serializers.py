from rest_framework import serializers
from .models import *

class TeamSerializer(serializers.ModelSerializer):
    team = serializers.CharField(required=True)

    class Meta:
        model = team
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    project = serializers.CharField(required=True)

    class Meta:
        model = project
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = member
        fields = '__all__'