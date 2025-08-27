import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'upsi_test.settings')
django.setup()

from mocktest.models import TestPaper, Question

# Create 10 test papers
papers_data = [
    {"title": "UPSI Mock Test - Paper 1", "description": "Comprehensive test covering all four sections with balanced difficulty level"},
    {"title": "UPSI Mock Test - Paper 2", "description": "Focus on current affairs and constitutional law with moderate difficulty"},
    {"title": "UPSI Mock Test - Paper 3", "description": "Emphasis on numerical ability and logical reasoning skills"},
    {"title": "UPSI Mock Test - Paper 4", "description": "Hindi language proficiency and general knowledge assessment"},
    {"title": "UPSI Mock Test - Paper 5", "description": "Advanced level test with challenging questions from all sections"},
    {"title": "UPSI Mock Test - Paper 6", "description": "Practice test focusing on UP state-specific knowledge"},
    {"title": "UPSI Mock Test - Paper 7", "description": "Balanced mix of easy to moderate level questions"},
    {"title": "UPSI Mock Test - Paper 8", "description": "Recent pattern based questions with updated syllabus"},
    {"title": "UPSI Mock Test - Paper 9", "description": "Time management focused test with quick-solve questions"},
    {"title": "UPSI Mock Test - Paper 10", "description": "Final revision test covering entire UPSI syllabus"}
]

# Sample questions for each section
sample_questions = {
    'general_hindi': [
        {
            'text': 'निम्नलिखित में से कौन सा शब्द "आकाश" का पर्यायवाची है?',
            'option_a': 'पृथ्वी',
            'option_b': 'गगन',
            'option_c': 'समुद्र',
            'option_d': 'पर्वत',
            'correct_answer': 'B'
        },
        {
            'text': '"सूर्य" का विलोम शब्द क्या है?',
            'option_a': 'चन्द्र',
            'option_b': 'तारा',
            'option_c': 'प्रकाश',
            'option_d': 'अंधकार',
            'correct_answer': 'A'
        }
    ],
    'law_constitution': [
        {
            'text': 'भारतीय संविधान में कुल कितने अनुच्छेद हैं?',
            'option_a': '395',
            'option_b': '396',
            'option_c': '448',
            'option_d': '450',
            'correct_answer': 'C'
        },
        {
            'text': 'भारत का सर्वोच्च न्यायालय कहाँ स्थित है?',
            'option_a': 'मुंबई',
            'option_b': 'नई दिल्ली',
            'option_c': 'कोलकाता',
            'option_d': 'चेन्नई',
            'correct_answer': 'B'
        }
    ],
    'general_knowledge': [
        {
            'text': 'उत्तर प्रदेश की राजधानी कौन सी है?',
            'option_a': 'कानपुर',
            'option_b': 'आगरा',
            'option_c': 'लखनऊ',
            'option_d': 'वाराणसी',
            'correct_answer': 'C'
        },
        {
            'text': 'भारत के प्रथम प्रधानमंत्री कौन थे?',
            'option_a': 'महात्मा गांधी',
            'option_b': 'जवाहरलाल नेहरू',
            'option_c': 'सरदार पटेल',
            'option_d': 'डॉ. राजेंद्र प्रसाद',
            'correct_answer': 'B'
        }
    ],
    'numerical_mental': [
        {
            'text': '25 का 40% कितना होगा?',
            'option_a': '8',
            'option_b': '10',
            'option_c': '12',
            'option_d': '15',
            'correct_answer': 'B'
        },
        {
            'text': 'यदि A = 1, B = 2, C = 3... तो WORD का मान क्या होगा?',
            'option_a': '72',
            'option_b': '73',
            'option_c': '74',
            'option_d': '75',
            'correct_answer': 'A'
        }
    ]
}

print("Creating test papers and questions...")

for paper_data in papers_data:
    paper = TestPaper.objects.create(**paper_data)
    print(f"Created: {paper.title}")
    
    # Add 40 questions for each section (160 total per paper)
    for section, questions in sample_questions.items():
        for i in range(40):
            # Cycle through sample questions
            q_data = questions[i % len(questions)]
            Question.objects.create(
                paper=paper,
                section=section,
                text=f"{q_data['text']} (Q{i+1})",
                option_a=q_data['option_a'],
                option_b=q_data['option_b'],
                option_c=q_data['option_c'],
                option_d=q_data['option_d'],
                correct_answer=q_data['correct_answer'],
                subject=section.replace('_', ' ').title()
            )

print("✅ Successfully created 10 test papers with 160 questions each!")
print("📊 Total: 1600 questions across 4 sections (40 per section)")