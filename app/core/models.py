from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from core.utils import BaseModel
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.

class User(AbstractUser):
    """
    Custom user model
    """
    email = models.EmailField(
        max_length=255,
        unique=True,
        help_text="Enter your email address",
        verbose_name="email address",
        db_index=True
    )
    phone = models.CharField(
        max_length=10,
        help_text="Enter your phone number",
        db_index=True
    )
    age = models.CharField(
        max_length=3,
        help_text="Enter your age"
    )
    profile_pic = models.ImageField(
        upload_to='profile_pics/', 
        blank=True, 
        null=True,
        help_text="Upload your profile picture"
    )
    address = models.TextField(
        blank=True, 
        null=True,
        help_text="Enter your address"
    )
    city = models.CharField(
        max_length=50, 
        blank=True, 
        null=True,
        help_text="Enter your city"
    )
    access_code = models.CharField(
        max_length=6,
        help_text="User access code"
    )
    is_verified = models.BooleanField(
        default=False,
        help_text="Account verification status"
    )
    trusted_ip = ArrayField(
        models.CharField(max_length=15),
        verbose_name="trusted ip",
        blank=True,
        null=True
    )
    last_online = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Last online time"
    )

class ManagerUser(models.Model):
    """
    Manager user model
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="manager_user",
        help_text="Manager user",
        verbose_name="manager user",
        db_index=True
    )
    is_staff = True
    is_superuser = True

class Doctor(models.Model):
    """
    Doctor user model
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="doctor_user",
        help_text="Doctor user",
        db_index = True
    )
    branch = models.ForeignKey(
        "Branch",
        on_delete=models.CASCADE,
        related_name="branch",
        help_text="Doctor branch",
        verbose_name="doctor branch",
        db_index=True
    )


    UNIQUE_FIELDS = ['phone']

    class Meta:
        db_table = "core_doctor"
        verbose_name = "doctor_user"
        verbose_name_plural = "doctor_users"

    def __str__(self):
        return f"Dr.{self.first_name} {self.last_name}"
    
    @staticmethod
    def get_status():
        return "dr"

    @staticmethod
    def get_doctor_via_branch(branch):
        return Doctor.objects.filter(branch=branch).all()


class Patient(models.Model):
    """
    Patient user model
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="patient_user",
        help_text="Patient user",
        verbose_name="patient user",
        db_index=True
    )
    identity_number = models.CharField(
        max_length=11,
        help_text="Enter your identity number",
        db_index=True
    )

    credit_card = models.JSONField(
        blank=True,
        null=True,
        help_text="Patient credit card information",
        verbose_name="patient credit card information"
    )
    medical_history = models.JSONField(
        blank=True,
        null=True,
        help_text="Patient medical history",
        verbose_name="patient medical history"
    )
    medication_history = models.JSONField(
        blank=True,
        null=True,
        help_text="Patient medication history",
        verbose_name="patient medication history"
    )
    allergies = models.JSONField(
        blank=True,
        null=True,
        help_text="Patient allergies",
        verbose_name="patient allergies"
    )
    emergency_contact = models.JSONField(
        blank=True,
        null=True,
        help_text="Patient emergency contact",
        verbose_name="patient emergency contact"
    )
    membership = models.OneToOneField(
        "Membership",
        on_delete=models.DO_NOTHING,
        related_name="membership",
        help_text="Patient membership",
        verbose_name="patient membership",
        null=True,
        blank=True
    )


    UNIQUE_FIELDS = ['phone', 'identity_number']

    class Meta:
        db_table = "core_patient"
        verbose_name = "patient_user"
        verbose_name_plural = "patient_users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

    @staticmethod
    def get_patient_via_age(age):
        return Patient.objects.filter(age=age).all()
    
    @staticmethod
    def get_patient_via_age_and_city(age, city):
        return Patient.objects.filter(age=age, city=city).all()
    
    @staticmethod
    def get_patient_via_city(city):
        return Patient.objects.filter(city=city).all()
    
    
class Branch(BaseModel):
    """
    Doctor branch model
    """  
    name = models.CharField(
        max_length=50,
        help_text="Branch name",
        verbose_name="branch name",
        unique=True
    )

    def __str__(self):
        return self.name
    
    
class Membership(BaseModel): 
    """
    Patient membership model
    """
    name = models.CharField(
        max_length=50,
        help_text="Membership name",
        verbose_name="membership name",
        unique=True,
        db_index=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Membership price",
        verbose_name="membership price"
    )
    duration = models.SmallIntegerField(
        help_text="Membership duration as day",
        verbose_name="membership duration as day"
    )
    discount = models.SmallIntegerField(
        null=True,
        blank=True,
        help_text="Membership discount as percentage",
        verbose_name="membership discount as percentage"
    )
    description = models.TextField(
        help_text="Membership description",
        verbose_name="membership description"
    )

    def __str__(self):
        return self.name

