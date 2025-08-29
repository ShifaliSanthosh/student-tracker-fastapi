**Student Performance Tracker API**

A RESTful API built with FastAPI to manage students, their scores, and academic performance — including graduate student support, subject-wise top scorers, and department average scores.

---

**Features**

- Add, view, and delete students
- Add/update subject scores
- View average scores per student
- Find top scorer in a subject
- Get department average
- Supports SQLite (dev) and PostgreSQL (prod-ready)

---

**1. Clone the Repo**

git clone https://github.com/ShifaliSanthosh/student-tracker-fastapi.git

cd student-tracker-fastapi


**2. Create Virtual Environment**
   
python -m venv .venv
.venv\Scripts\activate         # Windows

**3. Install Dependencies**

pip install -r requirements.txt

**4. Run the server**

uvicorn app.main:app --reload

