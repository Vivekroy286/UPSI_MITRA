import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'upsi_test.settings')
django.setup()

from mocktest.models import Question

# Sample UPSI questions
questions = [
    {
        'text': 'Who is known as the Father of the Indian Constitution?',
        'option_a': 'Mahatma Gandhi',
        'option_b': 'Dr. B.R. Ambedkar',
        'option_c': 'Jawaharlal Nehru',
        'option_d': 'Sardar Patel',
        'correct_answer': 'B',
        'subject': 'Indian Polity'
    },
    {
        'text': 'The Tropic of Cancer passes through which Indian state?',
        'option_a': 'Rajasthan',
        'option_b': 'Gujarat',
        'option_c': 'Madhya Pradesh',
        'option_d': 'All of the above',
        'correct_answer': 'D',
        'subject': 'Geography'
    },
    {
        'text': 'Which article of the Indian Constitution deals with Right to Education?',
        'option_a': 'Article 19',
        'option_b': 'Article 21A',
        'option_c': 'Article 25',
        'option_d': 'Article 32',
        'correct_answer': 'B',
        'subject': 'Indian Polity'
    },
    {
        'text': 'The Battle of Plassey was fought in which year?',
        'option_a': '1757',
        'option_b': '1764',
        'option_c': '1761',
        'option_d': '1767',
        'correct_answer': 'A',
        'subject': 'History'
    },
    {
        'text': 'Which is the largest state in India by area?',
        'option_a': 'Madhya Pradesh',
        'option_b': 'Uttar Pradesh',
        'option_c': 'Rajasthan',
        'option_d': 'Maharashtra',
        'correct_answer': 'C',
        'subject': 'Geography'
    }
]

for q_data in questions:
    Question.objects.create(**q_data)

print("Sample questions loaded successfully!")