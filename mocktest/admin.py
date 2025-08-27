from django.contrib import admin
from .models import Question, TestResult

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'subject', 'correct_answer']
    list_filter = ['subject', 'correct_answer']

@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'score', 'total_questions', 'completed_at']
    list_filter = ['completed_at']