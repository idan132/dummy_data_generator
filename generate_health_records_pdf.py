from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Generate a single fake health record
def generate_health_record():
    return {
        'PatientID': fake.uuid4(),
        'FullName': fake.name(),
        'DOB': fake.date_of_birth(minimum_age=0, maximum_age=115).strftime('%Y-%m-%d'),
        'Gender': random.choice(['Male', 'Female', 'Other']),
        'Diagnosis': random.choice(['Asthma', 'Diabetes', 'Flu', 'COVID-19', 'Hypertension']),
        'Treatment': 'Treatment details for condition.',
        'MedicationPrescribed': random.choice(['Medication A', 'Medication B', 'Medication C', 'Medication D'])
    }

# Create a PDF with neatly formatted fake health records
def create_neat_pdf(path):
    doc = SimpleDocTemplate(path, pagesize=letter)
    styles = getSampleStyleSheet()
    Story = []
    
    records_to_generate = 10  # Adjust the number of records as needed
    
    for _ in range(records_to_generate):
        record = generate_health_record()
        record_text = f"""
        Patient ID: {record['PatientID']}
        Name: {record['FullName']}
        DOB: {record['DOB']}
        Gender: {record['Gender']}
        Diagnosis: {record['Diagnosis']}
        Treatment: {record['Treatment']}
        Medication Prescribed: {record['MedicationPrescribed']}
        """
        Story.append(Paragraph(record_text, styles["Normal"]))
        Story.append(Spacer(1, 12))  # Add space between records

    doc.build(Story)

# Specify the path where you want to save the PDF
output_path = './fake_health_records_neat.pdf'
create_neat_pdf(output_path)
