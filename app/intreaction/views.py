from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    AllowAny
)


class DoctorScoreView(views.APIView):
    """
    Doctor score view
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        Create doctor score
        """
        return Response(status=status.HTTP_200_OK)

    