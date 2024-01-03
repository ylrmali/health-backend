from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime, timedelta


# Create your models here.


class DoctorScore(models.Model):
    """
    Doctor score model
    """
    doctor = models.ForeignKey(
        'core.Doctor',
        on_delete=models.CASCADE,
        related_name='doctor_score'
    )
    patient = models.ForeignKey(
        'core.Patient',
        on_delete=models.CASCADE,
        related_name='patient_score'
    )
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    class Meta:
        db_table = 'doctor_score'

    def get_doctor_avg_score(self):
        """
        Get doctor avg score
        """
        return DoctorScore.objects.filter(doctor=self.doctor).aggregate(models.Avg('score'))['score__avg']
    

class Report(models.Model):
    """
    Doctor report model
    """
    reporter = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        related_name='reporter_user'
    )
    reported = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        related_name='reported_user'
    )
    subject = models.CharField(max_length=120)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'report'

    def can_report_again(self):
        """
        Check if user can report again
        Check date and count
        Date must be 7 days before
        Count must be less than 1
        """
        return Report.objects.filter(
            reporter=self.reporter,
            reported=self.reported,
            date__gte=datetime.now() - timedelta(days=7)
        ).count() < 1
    

class Post(models.Model):
    """
    User's post model
    """
    user = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        related_name='patient_post'
    )
    subject = models.CharField(max_length=120)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'post'

    def get_user_post(self):
        # Get patient posts
        return Post.objects.filter(user=self.user)


class Comment(models.Model):
    """
    Post's comment model
    """
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='post_comment'
    )
    user = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        related_name='user_comment',
        null=True,
        blank=True
    )
    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comment'

    def get_post_commnet(self):
        # Get post comments
        return Comment.objects.filter(post=self.post)
    

class Notification(models.Model):
    """
    Notification model
    """
    sender = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        related_name='sender_user'
    )
    reciever = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        related_name='reciever_user'
    )
    detail = models.JSONField()
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        db_table = 'notification'
    

    
class ChatRoom(models.Model):
    """
    Chat model
    """
    sender = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        related_name='sender_chat'
    )
    reciever = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        related_name='reciever_chat'
    )
    is_limitted = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        db_table = 'chat'


class Message(models.Model):
    """
    Message model
    """
    chat_room = models.ForeignKey(
        'ChatRoom',
        on_delete=models.CASCADE,
        related_name='chat_room_message'
    )
    sender = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        related_name='sender_message'
    )
    reciever = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        related_name='reciever_message'
    )
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        db_table = 'message'


