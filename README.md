# Grade Tracker
A CLI application to manage student grades with SQLite storage and AI-powered insights.

# Features
What can it do? List the main things:

# Tech stack

Python 3.x
SQLite (sqlite3)
requests
python-dotenv
Anthropic API (coming in Phase 2)
Enroll students across multiple classrooms
Track marks, calculate percentage and grade automatically
Persistent SQLite storage with proper relational schema
Delete students, update marks
REST API integration
(Soon) AI-powered class performance summaries

## Project Structure

gradeTracker/
├── models/
│   ├── student.py
│   └── scholarship_student.py
├── storage/
│   ├── json_storage.py
│   └── sqlite_storage.py
├── classroom.py
├── cli.py
├── .env.example
└── README.md

## Setup and Run

# clone the repo
git clone https://github.com/kaushal122/gradeTracker.git
cd gradeTracker

# create virtual environment
python -m venv .venv
source .venv/bin/activate  # Mac/Linux

# install dependencies
pip install -r requirements.txt

# create .env file
cp .env.example .env
# edit .env and add your DB path

# run
python cli.py


# Environment Variabe
dbPath=./storage/classRoom.db


# What I learned (optional but impressive for recruiters)

OOP design with inheritance and properties
Multi-file Python project structure
SQLite relational schema with foreign keys and composite unique constraints
REST API integration with requests library
Secure API key management with dotenv




## Grading Scale

| Percentage | Grade |
|-----------|-------|
| >= 60%    | First |
| >= 50%    | Second |
| < 50%     | Better Luck Next Time |
