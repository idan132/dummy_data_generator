import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Choose the number of records
num_records = 100

data = {
    'PatientID': [fake.uuid4() for _ in range(num_records)],
    'FullName': [fake.name() for _ in range(num_records)],
    'DOB': [fake.date_of_birth(minimum_age=0, maximum_age=115).strftime('%Y-%m-%d') for _ in range(num_records)],
    'Gender': [random.choice(['Male', 'Female', 'Other']) for _ in range(num_records)],
    'Diagnosis': [random.choice(['Asthma', 'Diabetes', 'Flu', 'COVID-19', 'Hypertension']) for _ in range(num_records)],
    'Treatment': ['Treatment details for ' + diagnosis for diagnosis in np.random.choice(['Asthma', 'Diabetes', 'Flu', 'COVID-19', 'Hypertension'], num_records)],
    'MedicationPrescribed': [random.choice(['Medication A', 'Medication B', 'Medication C', 'Medication D']) for _ in range(num_records)]
}

df = pd.DataFrame(data)

# Save to a CSV file
df.to_csv('./fake_health_records.csv', index=False)
