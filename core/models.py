from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class User(AbstractUser):
    ROLE_CHOICES = [
        ('professor', 'Professor'),
        ('attendee', 'Attendee'),
        ('facilitator', 'Facilitator'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_image = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

# Course Model
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    facilitator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    max_enrollment = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive'), ('completed', 'Completed')])

# Session Model
class Session(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sessions')
    session_date = models.DateTimeField()
    duration = models.IntegerField()
    location = models.CharField(max_length=255, blank=True, null=True)
    session_type = models.CharField(max_length=20, choices=[('online', 'Online'), ('offline', 'Offline'), ('hybrid', 'Hybrid')])
    agenda = models.TextField(blank=True, null=True)

# Enrollment Model
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('enrolled', 'Enrolled'), ('completed', 'Completed'), ('dropped', 'Dropped')])
    progress = models.FloatField(default=0)

# Feedback Model
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='feedbacks')
    comments = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

# Certificate Model
class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certificates')
    issued_date = models.DateTimeField(auto_now_add=True)
    certificate_image = models.URLField()
    is_revoked = models.BooleanField(default=False)

# Material Model
class Material(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file_type = models.CharField(max_length=20)
    file_path = models.URLField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='materials')
    is_public = models.BooleanField(default=False)

# Quiz Model
class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=255)
    total_marks = models.IntegerField()
    pass_marks = models.IntegerField()
    time_limit = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

# Question Model
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    question_type = models.CharField(max_length=20, choices=[('multiple_choice', 'Multiple Choice'), ('true_false', 'True/False'), ('short_answer', 'Short Answer')])

# Option Model
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=255)
    is_correct = models.BooleanField()

# User Quiz Response Model
class UserQuizResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_responses')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='responses')
    score = models.IntegerField()

# Notification Model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)

# User Role and Permission Model
class UserRolePermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='role_permissions')
    can_create_course = models.BooleanField(default=False)
    can_enroll = models.BooleanField(default=True)
    can_provide_feedback = models.BooleanField(default=True)

# Payment Transaction Model (if applicable)
class PaymentTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_status = models.CharField(max_length=20, choices=[('completed', 'Completed'), ('pending', 'Pending'), ('failed', 'Failed')])
    payment_method = models.CharField(max_length=20, choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal'), ('bank_transfer', 'Bank Transfer')])
