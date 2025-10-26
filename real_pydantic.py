from pydantic import BaseModel, EmailStr,Field
from typing import List, Dict, Optional,Annotated

# ✅ Pydantic v2 model
class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    age: int
    weight: float = Field(gt=0)
    married: bool = False  # Default False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]
    Email: EmailStr = "abf@gmail.com"

# ✅ Function to print patient data
def insert_patient_data(patient: Patient):
    print("Name:", patient.name)
    print("Age:", patient.age)
    print("Weight:", patient.weight)
    print("Married:", patient.married)
    print("Allergies:", patient.allergies)
    print("Contact Details:", patient.contact_details)
    print("Email:", patient.Email)
    print("-" * 40)

# ✅ Sample list of patients
patients_info = [
    {
        "name": "Pulkit Sharma",
        "age": 25,
        "weight": 70.5,
        "married": False,
        "allergies": ["Peanuts", "Dust"],
        "contact_details": {
            "email": "pulkit@example.com",
            "phone": "+91-9876543210"
        },
        "Email": "def@gmail.com",
    },
    {
        "name": "Riya Mehta",
        "age": 30,
        "weight": 60.2,
        "married": True,
        "allergies": ["Pollution"],
        "contact_details": {
            "email": "riya.mehta@example.com",
            "phone": "+91-9123456780"
        }
    },
    {
        "name": "Aman Verma",
        "age": 40,
        "weight": 82.0,
        "married": True,
        "contact_details": {
            "email": "amanv@example.com",
            "phone": "+91-9988776655"
        }
    },
    {
        "name": "Neha Singh",
        "age": 22,
        "weight": 55.8,
        "married": False,
        "allergies": [],
        "contact_details": {
            "email": "nehasingh@example.com",
            "phone": "+91-9090909090"
        }
    },
    {
        "name": "Rohit Das",
        "age": 28,
        "weight": 68.4,
        "married": False,
        "allergies": ["Milk"],
        "contact_details": {
            "email": "rohitdas@example.com",
            "phone": "+91-9801122334"
        }
    }
]

# ✅ Loop through patients and print data
for info in patients_info:
    patient_obj = Patient(**info)
    insert_patient_data(patient_obj)
