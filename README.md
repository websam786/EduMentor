# 🎓 EduMentor AI

Your Personal AI-Powered Academic Mentor

## 📌 About the Project

EduMentor AI is an AI-powered student performance analysis application.

Students enter their marks, and the application calculates their overall percentage and uses an LLM to generate personalized academic feedback.

## ✨ Features

- Student performance analysis
- Automatic percentage calculation
- Input validation using Pydantic
- AI-generated performance summary
- Identification of student strengths
- Areas for improvement
- Personalized study plan
- Premium Streamlit dashboard
- FastAPI backend

## 🛠️ Technologies Used

- Python
- FastAPI
- Pydantic
- Streamlit
- OpenAI API
- Git
- GitHub

## 🏗️ Architecture

Student
↓
Streamlit Frontend
↓
FastAPI Backend
↓
Pydantic Validation
↓
Python Performance Calculation
↓
OpenAI LLM
↓
AI Feedback
↓
Streamlit Dashboard

## 🚀 How It Works

1. Student enters their subject marks.
2. FastAPI receives and validates the data.
3. Python calculates the overall percentage.
4. The validated student information is sent to the OpenAI LLM.
5. The LLM generates structured academic feedback.
6. Streamlit displays the performance report.

## 🔐 Environment Variables

The OpenAI API key is stored securely using an environment variable.

```text
OPENAI_API_KEY=your_api_key_here