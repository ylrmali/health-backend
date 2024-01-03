# Generated by Django 4.2 on 2024-01-01 11:44

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('email', models.EmailField(db_index=True, help_text='Enter your email address', max_length=255, unique=True, verbose_name='email address')),
                ('phone', models.CharField(db_index=True, help_text='Enter your phone number', max_length=10)),
                ('age', models.CharField(help_text='Enter your age', max_length=3)),
                ('profile_pic', models.ImageField(blank=True, help_text='Upload your profile picture', null=True, upload_to='profile_pics/')),
                ('access_code', models.CharField(help_text='User access code', max_length=6)),
                ('is_verified', models.BooleanField(default=False, help_text='Account verification status')),
                ('trusted_ip', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15), blank=True, null=True, size=None, verbose_name='trusted ip')),
            ],
            options={
                'db_table': 'base_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Alergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Alergies name', max_length=50, unique=True, verbose_name='alergies name')),
                ('description', models.TextField(help_text='Alergies description', verbose_name='alergies description')),
            ],
            options={
                'verbose_name': 'alergies',
                'verbose_name_plural': 'alergies',
                'db_table': 'alergies',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Branch name', max_length=50, unique=True, verbose_name='branch name')),
            ],
            options={
                'verbose_name': 'branch',
                'verbose_name_plural': 'branches',
                'db_table': 'branch',
            },
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(help_text='Clinic name', max_length=50, unique=True, verbose_name='clinic name')),
                ('address', models.TextField(help_text='Clinic address', verbose_name='clinic address')),
                ('city', models.CharField(help_text='Clinic city', max_length=50, verbose_name='clinic city')),
                ('phone', models.CharField(help_text='Clinic phone', max_length=10, verbose_name='clinic phone')),
                ('email', models.EmailField(help_text='Clinic email', max_length=255, verbose_name='clinic email')),
            ],
            options={
                'verbose_name': 'clinic',
                'verbose_name_plural': 'clinics',
                'db_table': 'clinic',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(blank=True, decimal_places=1, help_text='Doctor score', max_digits=2, null=True, verbose_name='doctor score')),
                ('branch', models.ForeignKey(help_text='Doctor branch', on_delete=django.db.models.deletion.CASCADE, related_name='branch', to='core.branch', verbose_name='doctor branch')),
                ('user', models.OneToOneField(help_text='Doctor user', on_delete=django.db.models.deletion.CASCADE, related_name='doctor_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'doctor_user',
                'verbose_name_plural': 'doctor_users',
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Medicine name', max_length=50, unique=True, verbose_name='medicine name')),
                ('description', models.TextField(help_text='Medicine description', verbose_name='medicine description')),
                ('image', models.ImageField(blank=True, help_text='Medicine image', null=True, upload_to='medicines/', verbose_name='medicine image')),
            ],
            options={
                'verbose_name': 'medicine',
                'verbose_name_plural': 'medicines',
                'db_table': 'medicine',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity_card', models.JSONField()),
                ('credit_card', models.JSONField(blank=True, help_text='Patient credit card information', null=True, verbose_name='patient credit card information')),
                ('emergency_contact', models.JSONField(blank=True, help_text='Patient emergency contact', null=True, verbose_name='patient emergency contact')),
                ('address', models.TextField(blank=True, help_text='Enter your address', null=True)),
                ('city', models.CharField(blank=True, help_text='Enter your city', max_length=50, null=True)),
                ('allergies', models.ManyToManyField(help_text='Patient allergies', related_name='allergies', to='core.alergy', verbose_name='patient allergies')),
                ('medicine', models.ManyToManyField(help_text='Patient medicine', related_name='medicine', to='core.medicine', verbose_name='patient medicine')),
                ('user', models.OneToOneField(help_text='Patient user', on_delete=django.db.models.deletion.CASCADE, related_name='patient_user', to=settings.AUTH_USER_MODEL, verbose_name='patient user')),
            ],
            options={
                'verbose_name': 'patient_user',
                'verbose_name_plural': 'patient_users',
                'db_table': 'patient',
            },
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Symtomp name', max_length=50, unique=True, verbose_name='symtomp name')),
                ('description', models.TextField(help_text='Symtomp description', verbose_name='symtomp description')),
            ],
            options={
                'verbose_name': 'symptom',
                'verbose_name_plural': 'symptoms',
                'db_table': 'symptom',
            },
        ),
        migrations.CreateModel(
            name='Vital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('weight', models.CharField(max_length=3)),
                ('height', models.CharField(max_length=3)),
                ('blood_pressure', models.CharField(max_length=3)),
                ('blood_sugar', models.CharField(max_length=3)),
                ('heart_rate', models.CharField(max_length=3)),
                ('body_temperature', models.CharField(max_length=3)),
                ('oxygen_in_blood', models.CharField(max_length=3)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(help_text='Vital patient', on_delete=django.db.models.deletion.CASCADE, related_name='patient_vital', to='core.patient', verbose_name='vital patient')),
            ],
            options={
                'verbose_name': 'vital',
                'verbose_name_plural': 'vitals',
                'db_table': 'vital',
            },
        ),
        migrations.CreateModel(
            name='Radiological',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('images', models.JSONField()),
                ('description', models.CharField(help_text='Radiological description', max_length=250, verbose_name='radiological description')),
                ('report', models.TextField(help_text='Radiological report', verbose_name='radiological report')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(help_text='Radiological patient', on_delete=django.db.models.deletion.CASCADE, related_name='patient_radiological', to='core.patient', verbose_name='radiological patient')),
            ],
            options={
                'verbose_name': 'radiological',
                'verbose_name_plural': 'radiologicals',
                'db_table': 'radiological',
            },
        ),
        migrations.CreateModel(
            name='ManagerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(help_text='Manager user', on_delete=django.db.models.deletion.CASCADE, related_name='manager_user', to=settings.AUTH_USER_MODEL, verbose_name='manager user')),
            ],
            options={
                'db_table': 'manager',
            },
        ),
        migrations.CreateModel(
            name='HowYouFeel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('symptom_score', models.JSONField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(help_text='How you feel patient', on_delete=django.db.models.deletion.CASCADE, related_name='patient_how_you_feel', to='core.patient', verbose_name='how you feel patient')),
                ('symptom', models.ManyToManyField(help_text='How you feel symptom', related_name='symptom', to='core.symptom', verbose_name='how you feel symptom')),
            ],
            options={
                'verbose_name': 'how_you_feel',
                'verbose_name_plural': 'how_you_feels',
                'db_table': 'how_you_feel',
            },
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('diagnosis', models.TextField(help_text='Examination diagnosis', verbose_name='examination diagnosis')),
                ('prescription', models.TextField(help_text='Examination prescription', verbose_name='examination prescription')),
                ('examination_date', models.DateTimeField(help_text='Examination date', verbose_name='examination date')),
                ('score', models.CharField(blank=True, max_length=1, null=True)),
                ('clinic', models.ForeignKey(help_text='Examination clinic', on_delete=django.db.models.deletion.CASCADE, related_name='examination_clinic', to='core.clinic', verbose_name='examination clinic')),
                ('doctor', models.ForeignKey(help_text='Examination doctor', on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='core.doctor', verbose_name='examination doctor')),
                ('patient', models.ForeignKey(help_text='Examination patient', on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='core.patient', verbose_name='examination patient')),
            ],
            options={
                'verbose_name': 'examination',
                'verbose_name_plural': 'examinations',
                'db_table': 'examination',
            },
        ),
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('short_description', models.CharField(help_text='Analysis short description', max_length=50, verbose_name='analysis short description')),
                ('description', models.TextField(help_text='Analysis description', verbose_name='analysis description')),
                ('test_result', models.JSONField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(help_text='Analysis patient', on_delete=django.db.models.deletion.CASCADE, related_name='patient_analysis', to='core.patient', verbose_name='analysis patient')),
            ],
            options={
                'verbose_name': 'analysis',
                'verbose_name_plural': 'analyses',
                'db_table': 'analysis',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='clinic',
            field=models.ForeignKey(help_text='User clinic', on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_clinic', to='core.clinic', verbose_name='user clinic'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
