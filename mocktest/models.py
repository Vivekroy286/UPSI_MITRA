from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random
from datetime import timedelta

class TestPaper(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Question(models.Model):
    SECTION_CHOICES = [
        ('general_hindi', 'General Hindi'),
        ('law_constitution', 'Law & Constitution'),
        ('general_knowledge', 'General Knowledge'),
        ('numerical_mental', 'Numerical & Mental Ability'),
    ]
    
    paper = models.ForeignKey(TestPaper, on_delete=models.CASCADE, related_name='questions', default=1)
    section = models.CharField(max_length=20, choices=SECTION_CHOICES, default='general_knowledge')
    text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    subject = models.CharField(max_length=100, default='General Knowledge')
    
    class Meta:
        ordering = ['section', 'id']

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True)
    is_phone_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.phone_number}"

class OTPVerification(models.Model):
    phone_number = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    
    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=5)
    
    @staticmethod
    def generate_otp():
        return str(random.randint(100000, 999999))
    
    def __str__(self):
        return f"{self.phone_number} - {self.otp}"

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paper = models.ForeignKey(TestPaper, on_delete=models.CASCADE, default=1)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    section_scores = models.JSONField(default=dict)
    completed_at = models.DateTimeField(auto_now_add=True)