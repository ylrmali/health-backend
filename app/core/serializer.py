from rest_framework import serializers
from core.models import (
    ManagerUser,
    Doctor,
    Patient,
    Branch,
    Membership
)
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

#* Core app serializers here
#* Serializewr convert python object to json

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'
        

class DoctorSerializer(serializers.ModelSerializer):
    '''
    Doctor serializer 
    '''
    user = serializers.SerializerMethodField()
    branch = serializers.SerializerMethodField()


    def get_user(self, obj):
        user = {
            "username": obj.user.username,
            "first_name": obj.user.first_name,
            "last_name": obj.user.last_name,
            "email": obj.user.email,
            "phone": obj.user.phone,
            "address": obj.user.address,
            "city": obj.user.city,
            "is_verified": obj.user.is_verified,
        }
        return user
    
    def get_branch(self, obj):
        branch = {
            "id": obj.branch.id,
            "name": obj.branch.name,
        }
        return branch
    
    class Meta:
        model = Doctor
        fields = '__all__'
        

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        user = {
            "username": obj.user.username,
            "first_name": obj.user.first_name,
            "last_name": obj.user.last_name,
            "email": obj.user.email,
            "phone": obj.user.phone,
            "address": obj.user.address,
            "city": obj.user.city,
            "is_verified": obj.user.is_verified,
        }
        return user
    
    class Meta:
        model = Patient
        fields = '__all__'

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'


class UserRegisterSerializer(serializers.Serializer):
    '''
    User register serializer
    '''
    
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    password = serializers.CharField(max_length=50)
    phone = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=150)
    city = serializers.CharField(max_length=50)

    validators = [
        UniqueValidator(
            queryset=get_user_model().objects.all(),
            message="This user already exists."
        )
    ]

class DoctorRegisterSerializer(serializers.Serializer):
    '''
    Doctor register serializer
    '''
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())


    validators = [
        UniqueValidator(
            queryset=Doctor.objects.all(),
            message="This doctor already exists."
        )
    ]

class PatientRegisterSerializer(serializers.Serializer):
    '''
    Patient register serializer
    '''
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    identity_number = serializers.CharField(max_length=11)

    validators = [
        UniqueValidator(
            queryset=Patient.objects.all(),
            message="This patient already exists."
        )
    ]
    