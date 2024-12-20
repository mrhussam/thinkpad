from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'members', MemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]