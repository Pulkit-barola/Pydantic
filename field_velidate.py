from pydantic import BaseModel, EmailStr,Field,field_validator
from typing import List, Dict, Optional,Annotated

class Patient(BaseModel):
    name: str
    age: int
    weight: float 
    married: bool = False  # Default False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]
    email: EmailStr;

    #@ -> it is decarotor
    @field_validator("email")
    @classmethod          #cls is class
    def email_validator(cls , value):
        valid_domans = ['hdfc.com','icici.com']

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domans:
            raise ValueError('Not a valid domain')

        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls , value):
        return value.upper()
    
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')
        
        #by default mode after hota ha 
        



def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)

#dekho agar sample data me string toh agar field validator me agar hamna before lagya toh ham type coerction seh pehla work hoga isma error bata dega 
#wahi agar hamna after kar toh wo pehla type coerction karega fir wo perform karega