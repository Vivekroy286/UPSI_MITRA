# UPSI Mock Test 2025

A Django web application for UPSI (Uttar Pradesh Sub Inspector) mock tests with TailwindCSS styling.

## Features

- User registration and authentication
- Mock test with timer (60 minutes)
- Multiple choice questions
- Score tracking and results history
- Admin interface for question management
- Responsive design with TailwindCSS

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create superuser (optional):
```bash
python manage.py createsuperuser
```

4. Load sample data:
```bash
python load_sample_data.py
```

5. Run the server:
```bash
python manage.py runserver
```

## Usage

1. Register a new account or login
2. Take mock tests with 20 questions
3. View your test results and progress
4. Admin can add/edit questions via `/admin/`

## Project Structure

- `mocktest/` - Main app with models, views, and URLs
- `templates/` - HTML templates with TailwindCSS
- `upsi_test/` - Django project settings