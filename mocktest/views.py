from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Question, TestResult, TestPaper, UserProfile, OTPVerification
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
import json
import re

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('papers')
            else:
                return render(request, 'login.html', {'error': 'Invalid email or password'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Email not registered'})
    
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Validate inputs
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already registered'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        
        # Create user and profile
        user = User.objects.create_user(username=username, email=email, password=password)
        UserProfile.objects.create(
            user=user,
            is_email_verified=True
        )
        
        login(request, user)
        return redirect('papers')
    
    return render(request, 'register.html')

@login_required
def papers_view(request):
    papers = TestPaper.objects.all()
    return render(request, 'papers.html', {'papers': papers})

@login_required
def test_instructions(request, paper_id):
    paper = get_object_or_404(TestPaper, id=paper_id)
    return render(request, 'test_instructions.html', {'paper': paper})

@login_required
def test_view(request, paper_id):
    paper = get_object_or_404(TestPaper, id=paper_id)
    questions = list(paper.questions.all()[:160].values())  # Convert to list for JSON
    language = request.GET.get('lang', 'english')
    return render(request, 'test.html', {'questions': json.dumps(questions), 'paper': paper, 'language': language})

@login_required
def submit_test(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        answers = data.get('answers', {})
        paper_id = data.get('paper_id')
        
        paper = get_object_or_404(TestPaper, id=paper_id)
        score = 0
        total = 0
        section_scores = {}
        
        for question_id, answer in answers.items():
            question = Question.objects.get(id=question_id)
            section = question.section
            
            if section not in section_scores:
                section_scores[section] = {'correct': 0, 'total': 0}
            
            section_scores[section]['total'] += 1
            total += 1
            
            if question.correct_answer == answer:
                score += 1
                section_scores[section]['correct'] += 1
        
        TestResult.objects.create(
            user=request.user,
            paper=paper,
            score=score,
            total_questions=total,
            section_scores=section_scores
        )
        
        return JsonResponse({'score': score, 'total': total, 'section_scores': section_scores})

@login_required
def results_view(request):
    results = TestResult.objects.filter(user=request.user).order_by('-completed_at')
    return render(request, 'results.html', {'results': results})

def logout_view(request):
    logout(request)
    return redirect('home')