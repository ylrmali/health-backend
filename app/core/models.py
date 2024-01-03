from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from core.utils import BaseModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

# Create your models here.

class User(AbstractUser):
    """
    Custom user model
    """
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    clinic = models.ForeignKey(
        "Clinic",
        on_delete=models.DO_NOTHING,
        related_name="user_clinic",
        help_text="User clinic",
        verbose_name="user clinic",
    )
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

    class Meta:
        db_table = "base_user"

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

    class Meta:
        db_table = "manager"


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
    score = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        help_text="Doctor score",
        verbose_name="doctor score",
        null=True,
        blank=True
    )


    UNIQUE_FIELDS = ['phone']

    class Meta:
        db_table = "doctor"
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
    identity_card = models.JSONField()
    credit_card = models.JSONField(
        blank=True,
        null=True,
        help_text="Patient credit card information",
        verbose_name="patient credit card information"
    )
    allergies = models.ManyToManyField(
        "Alergy",
        related_name="allergies",
        help_text="Patient allergies",
        verbose_name="patient allergies"
    )
    medicine = models.ManyToManyField(
        "Medicine",
        related_name="medicine",
        help_text="Patient medicine",
        verbose_name="patient medicine"
    )
    emergency_contact = models.JSONField(
        blank=True,
        null=True,
        help_text="Patient emergency contact",
        verbose_name="patient emergency contact"
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

    UNIQUE_FIELDS = ['phone', 'identity_number']

    class Meta:
        db_table = "patient"
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

    class Meta:
        db_table = "branch"
        verbose_name = "branch"
        verbose_name_plural = "branches"

    def __str__(self):
        return self.name


class Medicine(BaseModel):
    """
    Medicine model
    """
    name = models.CharField(
        max_length=50,
        help_text="Medicine name",
        verbose_name="medicine name",
        unique=True
    )
    description = models.TextField(
        help_text="Medicine description",
        verbose_name="medicine description"
    )
    image = models.ImageField(
        upload_to='medicines/', 
        blank=True, 
        null=True,
        help_text="Medicine image",
        verbose_name="medicine image"
    )

    class Meta:
        db_table = "medicine"
        verbose_name = "medicine"
        verbose_name_plural = "medicines"

    def __str__(self):
        return self.name


class Alergy(BaseModel):
    """
    Alergies model
    """
    name = models.CharField(
        max_length=50,
        help_text="Alergies name",
        verbose_name="alergies name",
        unique=True
    )
    description = models.TextField(
        help_text="Alergies description",
        verbose_name="alergies description"
    )

    class Meta:
        db_table = "alergies"
        verbose_name = "alergies"
        verbose_name_plural = "alergies"

    def __str__(self):
        return self.name


class Clinic(BaseModel):
    """
    Clinic model
    """
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    name = models.CharField(
        max_length=50,
        help_text="Clinic name",
        verbose_name="clinic name",
        unique=True
    )
    address = models.TextField(
        help_text="Clinic address",
        verbose_name="clinic address"
    )
    city = models.CharField(
        max_length=50,
        help_text="Clinic city",
        verbose_name="clinic city"
    )
    phone = models.CharField(
        max_length=10,
        help_text="Clinic phone",
        verbose_name="clinic phone"
    )
    email = models.EmailField(
        max_length=255,
        help_text="Clinic email",
        verbose_name="clinic email"
    )
    UNIQUE_FIELDS = ['name', 'uuid']

    class Meta:
        db_table = "clinic"
        verbose_name = "clinic"
        verbose_name_plural = "clinics"

    def __str__(self):
        return self.name  


class Examination(BaseModel):
    """
    Examination model
    Doktor muayenesi
    """
    patient = models.ForeignKey(
        "Patient",
        on_delete=models.CASCADE,
        related_name="patient",
        help_text="Examination patient",
        verbose_name="examination patient",
        db_index=True
    )
    doctor = models.ForeignKey(
        "Doctor",
        on_delete=models.CASCADE,
        related_name="doctor",
        help_text="Examination doctor",
        verbose_name="examination doctor",
        db_index=True
    )
    clinic = models.ForeignKey(
        "Clinic",
        on_delete=models.CASCADE,
        related_name="examination_clinic",
        help_text="Examination clinic",
        verbose_name="examination clinic",
        db_index=True
    )
    diagnosis = models.TextField( # doktor tanısı
        help_text="Examination diagnosis",
        verbose_name="examination diagnosis"
    )
    prescription = models.TextField( # doktor reçetesi
        help_text="Examination prescription",
        verbose_name="examination prescription"
    )
    examination_date = models.DateTimeField(
        help_text="Examination date",
        verbose_name="examination date"
    )
    score = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = "examination"
        verbose_name = "examination"
        verbose_name_plural = "examinations"

    def __str__(self):
        return f"{self.patient} {self.doctor} {self.clinic} {self.examination_date}"
    
    @staticmethod
    def get_examination_via_patient(patient):
        return Examination.objects.filter(patient=patient).all()
    
    @staticmethod
    def get_examination_via_doctor(doctor):
        return Examination.objects.filter(doctor=doctor).all()
    
    @staticmethod
    def get_examination_via_clinic(clinic):
        return Examination.objects.filter(clinic=clinic).all()
    
    @staticmethod
    def get_examination_via_date(examination_date):
        return Examination.objects.filter(examination_date=examination_date).all()
    
    @staticmethod
    def get_examination_via_patient_and_doctor(patient, doctor):
        return Examination.objects.filter(patient=patient, doctor=doctor).all()


class Vital(BaseModel):
    """
    Vital model
    Hayati değerler
    """
    patient = models.ForeignKey(
        "Patient",
        on_delete=models.CASCADE,
        related_name="patient_vital",
        help_text="Vital patient",
        verbose_name="vital patient",
        db_index=True
    )
    weight = models.CharField(max_length=3)
    height = models.CharField(max_length=3)
    blood_pressure = models.CharField(max_length=3)  # tansiyon
    blood_sugar = models.CharField(max_length=3)  # şeker
    heart_rate = models.CharField(max_length=3)  # nabız
    body_temperature = models.CharField(max_length=3)
    oxygen_in_blood = models.CharField(max_length=3)  # oksijen
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "vital"
        verbose_name = "vital"
        verbose_name_plural = "vitals"

    def __str__(self):
        return f"{self.patient}"


class Symptom(BaseModel):
    """
    Symptom model
    """
    name = models.CharField(
        max_length=50,
        help_text="Symtomp name",
        verbose_name="symtomp name",
        unique=True
    )
    description = models.TextField(
        help_text="Symtomp description",
        verbose_name="symtomp description"
    )
    UNIQUE_FIELDS = ['name']

    class Meta:
        db_table = "symptom"
        verbose_name = "symptom"
        verbose_name_plural = "symptoms"

    def __str__(self):
        return self.name
   
   
class HowYouFeel(BaseModel):
    """
    How you feel model
    Example usage: 
    {
        patient: 1,
        symptom: [1, 2, 3],
        symptom_score: {
            1: 5,
            2: 4,
            3: 3
        }
    }
    """
    patient = models.ForeignKey(
        "Patient",
        on_delete=models.CASCADE,
        related_name="patient_how_you_feel",
        help_text="How you feel patient",
        verbose_name="how you feel patient",
        db_index=True
    )
    symptom = models.ManyToManyField(
        "Symptom",
        related_name="symptom",
        help_text="How you feel symptom",
        verbose_name="how you feel symptom"
    )
    # every symptom has a score so use json field
    symptom_score = models.JSONField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "how_you_feel"
        verbose_name = "how_you_feel"
        verbose_name_plural = "how_you_feels"

    def __str__(self):
        return f"{self.patient}"
    
class Radiological(BaseModel):
    """
    Radiological images model
    Example usage:
    {
        patient: 1,
        images: [
            {
                image: "base64 image",
                description: "description"
            },
            {
                image: "base64 image",
                description: "description"
            }
        ],
        description: "description",
        report: "report"
    }
    """
    patient = models.ForeignKey(
        "Patient",
        on_delete=models.CASCADE,
        related_name="patient_radiological",
        help_text="Radiological patient",
        verbose_name="radiological patient",
        db_index=True
    )
    images = models.JSONField()  # radiolojik görüntüler. Birden fazla olabilir o yüzden json field.
    description = models.CharField(
        max_length=250,
        help_text="Radiological description",
        verbose_name="radiological description"
    )
    report = models.TextField(
        help_text="Radiological report",
        verbose_name="radiological report"
    )
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "radiological"
        verbose_name = "radiological"
        verbose_name_plural = "radiologicals"

    def __str__(self):
        return f"{self.patient}"
    

class Analysis(BaseModel):
    """
    Analysis model
    Patient result of analysis
    Example usage:
    {
        patient: 1,
        short_description: "Full blood count",
        description: "Full blood count long description",
        test_result: {
            "blood_count" : {
                "red_blood_cell" : 5,
                "white_blood_cell" : 4,
                "hemoglobin" : 3
            },
            "urine" : {
                "ph" : 5,
                "glucose" : 4,
                "protein" : 3
            }
        }
    }
    """
    patient = models.ForeignKey(
        "Patient",
        on_delete=models.CASCADE,
        related_name="patient_analysis",
        help_text="Analysis patient",
        verbose_name="analysis patient",
        db_index=True
    )
    short_description = models.CharField(
        max_length=50,
        help_text="Analysis short description",
        verbose_name="analysis short description"
    ) 
    description = models.TextField(
        help_text="Analysis description",
        verbose_name="analysis description"
    )
    test_result = models.JSONField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "analysis"
        verbose_name = "analysis"
        verbose_name_plural = "analyses"

    def __str__(self):
        return f"{self.patient} {self.date}"

