import os
import django
import pandas as pd

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interview_app.settings')
django.setup()

from questions.models import Language, Question

# Path to your CSV file
csv_file_path = 'interview_questions.csv'

# Function to load data from CSV using pandas
def load_data_from_csv(file_path):
    df = pd.read_csv(file_path)
    
    for index, row in df.iterrows():
        language_name = row['Language']
        question_text = row['Question']
        answer_text = row['Answer']
        
        # Get or create the Language object
        language, created = Language.objects.get_or_create(name=language_name)
        if created:
            print(f'Created language: {language_name}')
        
        # Create the Question object
        Question.objects.create(language=language, question_text=question_text, answer_text=answer_text)
        print(f'Added question to {language_name}: {question_text}')

# Load the data
load_data_from_csv(csv_file_path)

print('Data loading complete.')
