from django.urls import path
from rest_framework import routers
from core import views

app_name = 'core'

router = routers.DefaultRouter()
router.register(r'patient', views.PatientViewSet, basename='patient')
router.register(r'branch', views.BranchViewSet, basename='branch')


urlpatterns = [
    path('doctor/', views.DoctorListView.as_view(), name='doctor-list'),
    path('doctor/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('doctor/register/', views.DoctorRegisterView.as_view(), name='doctor-register'),
    path('patient/register/', views.PatientRegisterView.as_view(), name='user-register'),
]

urlpatterns += router.urls
