from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets, permissions
from .models import UserProfile
from .serializers import UserProfile, UserProfileSerializer, UserProfileListSerializer
from .permissions import IsEmailValidate
# Create your views here.


class UserProfileAPiViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsEmailValidate)
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        queryset = UserProfile.objects.filter(user=self.request.user)
        return queryset


class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser,)
    serializer_class = UserProfileListSerializer
