import os
from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from openai import OpenAI
app = FastAPI()
load_dotenv()
client= OpenAI()
print("OPENAI_API_KEY exists:", bool(os.getenv("OPENAI_API_KEY")))

class Student(BaseModel):
    name: str
    math: int = Field(ge=0, le=100)
    english: int = Field(ge=0, le=100)
    science: int = Field(ge=0, le=100)
    social: int = Field(ge=0, le=100)

class StudentFeedback(BaseModel):
    summary: str
    strength: str
    areas_to_improve: str
    study_plan: str   

@app.get("/")
def home():
    return {"message":"Welcome to Edumentor AI"}

@app.get("/student")
def student():
    return{"name": "Samiya", "age" : 38,"city" : "Kochi"}

@app.post("/analyze-student")
def analyze_student(student: Student):

    total=student.math + student.english + student.science + student.social
    percentage = total/4

    prompt = f"""
    You are Edumentor AI, a friendly and experienced academic mentor.

    Analyze this student's performance.
    
    Student information:
    Name: {student.name}
    Math: {student.math}
    English: {student.english}
    Science: {student.science}
    Social Studies: {student.social}
    Overall percentage: {percentage}%


    Instructions:
    - Be encouraging and positive.
    - Use simple language that a student can understand.
    -Identify the student's strongest subject.
    -Give practical study advice
    -Do not discourage or criticize the student.
    -Keep the response concise

    Format your response using headings:

    Summary:
    Strength:
    Areas to improve:
    Tomorrow's Study Plan
    """

    response = client.responses.parse(
        model="gpt-5-mini" ,
        input=prompt,
        text_format=StudentFeedback
    )

    return {
        "percentage" : percentage,
        "feedback" : response.output_parsed
    }
@app.get("/test-api")
def test_api():
    response = client.responses.create(
        model="gpt-5-mini",
        input="Say exactly: EduMentor AI connectionis successful"
    )
    return {"message": response.output_text}
