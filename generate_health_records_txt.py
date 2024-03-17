from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Function to generate a single fake health record
def generate_health_record():
    return f"""Patient ID: {fake.uuid4()}
Name: {fake.name()}
DOB: {fake.date_of_birth(minimum_age=0, maximum_age=115).strftime('%Y-%m-%d')}
Gender: {random.choice(['Male', 'Female', 'Other'])}
Diagnosis: {random.choice(['Asthma', 'Diabetes', 'Flu', 'COVID-19', 'Hypertension'])}
Treatment: Treatment details for condition.
Medication Prescribed: {random.choice(['Medication A', 'Medication B', 'Medication C', 'Medication D'])}
"""

# Function to create a text file with fake health records
def create_txt_file(path, num_records=10):
    with open(path, 'w') as file:
        for _ in range(num_records):
            record = generate_health_record()
            file.write(record + "\n")  # Add an extra newline for spacing between records

# Specify the file path where you want to save the text file
file_path = './fake_health_records.txt'
create_txt_file(file_path)

