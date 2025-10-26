

This repository contains a collection of practical examples for data validation in Python.

## 🔍 What’s inside

- `pydantic.py` – Basic Pydantic model definitions and examples  
- `field_validate.py` – Demonstrates field validators (`@field_validator`)  
- `model_validator.py` – Shows how to validate at the model level (e.g., cross-field validation)  
- `computed_field.py` – Example of computed/derived fields within a model  
- `real_pydantic.py` – Realistic usage: building a `Patient` model with validation, defaulting, and contact info  
- Other files/folders for tutorials and experiments  

## ✅ Key Features

- Use of Python type hints for model attributes (e.g., `str`, `int`, `float`, `list[str]`, `dict[str, str]`)  
- Email validation via the `EmailStr` type from Pydantic  
- Custom validators using `@field_validator` to enforce domains or derive values  
- Default values and optional fields (`Optional[T]`)  
- Demonstration of how invalid input is caught at runtime  
- Example of how to structure a project for learning and real-world usage  

## 🛠️ Requirements & Setup

1. Ensure you have **Python 3.11+** installed.  
2. Install Pydantic version 2:  
   pip install pydantic


Learnings & Concepts Covered

Defining Pydantic models with BaseModel

Enforcing built-in types and third-party types (e.g., EmailStr)

Using @field_validator to validate or transform input

Optional and default field values

Handling missing fields and type coercion

Structuring code for validation logic and different scenarios
