from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_no = models.CharField(max_length=100)
    enrollment_year = models.CharField(max_length=10)
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class Session(models.Model):
    title = models.CharField(max_length=100)
    purpose = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def start_datetime(self):
        return timezone.make_aware(datetime.combine(self.start_date, self.start_time))

    @property
    def end_datetime(self):
        return timezone.make_aware(datetime.combine(self.end_date, self.end_time))

    def is_active(self):
        now = timezone.now()
        return self.start_datetime <= now <= self.end_datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', symmetrical=False, related_name='friend_profiles')
    registration_number = models.CharField(max_length=9)
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender} to {self.recipient}: {self.content}"

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name

class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user} to {self.to_user}"