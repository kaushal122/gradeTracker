# Student Grade Tracker

A CLI-based student grading system built with Python OOP and SQLite.

## Features

- Enroll students with marks across 3 subjects
- Multiple classrooms with separate student lists
- Auto-assigned roll numbers (per classroom)
- View all results, percentages, and grades
- Find class topper
- Delete students and update marks
- Persistent storage with SQLite
- Scholarship eligibility check (First class = eligible)
- Random joke on exit

## Project Structure

```
GradingSystem/
├── models/
│   ├── studentClass.py              # Student base class (marks, avg, grade)
│   └── ScholarshipStudentClass.py   # Scholarship eligibility (inherits Student)
├── storage/
│   ├── sqlite_storage.py            # SQLite CRUD operations
│   └── jsonStorage.py               # JSON storage (legacy)
├── classRoomClass.py                # ClassRoom (enroll, topper, results)
└── cli.py                           # CLI entry point
```

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install python-dotenv requests
```

Create a `.env` file:

```
dbPath=storage/classRoom.db
```

## Usage

```bash
python cli.py
```

### Menu Options

1. **Enroll Students** - Add students with marks for 3 subjects
2. **Show All Results** - Display name, roll number, percentage, and grade
3. **Show Topper** - Display the student with highest percentage
4. **Load from DB** - Refresh student data from database
5. **Delete a Student** - Remove a student by roll number
6. **Update Marks** - Update marks for a student by roll number
7. **Exit** - Exit with a random joke

## Grading Scale

| Percentage | Grade |
|-----------|-------|
| >= 60%    | First |
| >= 50%    | Second |
| < 50%     | Better Luck Next Time |
