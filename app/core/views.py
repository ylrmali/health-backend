from django.shortcuts import render
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
from core.models import (
    User,
    ManagerUser,
    Doctor,
    Patient,
    Branch,
)
from core.serializer import (
    UserRegisterSerializer,
    DoctorSerializer,
    DoctorRegisterSerializer,
    PatientSerializer,
    BranchSerializer,
)

# Create your views here.

class DoctorListView(generics.ListAPIView):
    """
    Doctor viewset
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Doctor detail view
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    """
    Patient viewset
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def list(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated]
        return super().list(request, *args, **kwargs)


class BranchViewSet(viewsets.ModelViewSet):
    """
    Branch viewset
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def list(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated]
        return super().list(request, *args, **kwargs)
    

class DoctorRegisterView(views.APIView):
    """
    Doctor register view
    """

    def post(self, request, *args, **kwargs):
        # first create user
        user = User.objects.create_user(
            username=request.data.get('username'),
            email=request.data.get('email'),
            password=request.data.get('password'),
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name'),
            phone=request.data.get('phone'),
            address=request.data.get('address'),
            city=request.data.get('city')
        )
        user.save()
        # then create doctor
        data = {
            'user_id': user.id,
            'branch_id': request.data.get('branch')
        }

        doctor = Doctor.objects.create(**data)
        doctor.save()
        return Response("success", status=status.HTTP_201_CREATED)

class PatientRegisterView(views.APIView):
    '''
    Create new patiend user
    '''
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # first create user
        user = User.objects.create_user(
            username=request.data.get('username'),
            email=request.data.get('email'),
            password=request.data.get('password'),
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name'),
            phone=request.data.get('phone'),
            address=request.data.get('address'),
            city=request.data.get('city')
        )
        user.save()
        # then create patient
        data = {
            'user_id': user.id,
            'identity_number': request.data.get('identity_number'),
        }

        patient = Patient.objects.create(**data)
        patient.save()
        return Response("success", status=status.HTTP_201_CREATED)


