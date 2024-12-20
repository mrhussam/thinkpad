from rest_framework import viewsets
from .models import *
from .serializers import *

class TeamViewSet(viewsets.ModelViewSet):
    queryset = team.objects.all()
    serializer_class = TeamSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = project.objects.all()
    serializer_class = ProjectSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = member.objects.all()
    serializer_class = MemberSerializer