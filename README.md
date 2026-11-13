# Recruitment & Placement Management System (RPMS)

A Flask and MySQL application for managing student profiles, companies, job openings, applications, interviews, offers and placements.

## Technology

- HTML, CSS and JavaScript
- Python 3.10+
- Flask
- MySQL 8.0+
- mysql-connector-python
- Werkzeug password hashing

## Project structure

```text
RPMS/
├── main.py
├── .env.example
├── requirements.txt
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   ├── routes/
│   ├── service/
│   ├── dao/
│   ├── model/
│   ├── util/
│   └── exception/
├── frontend/
│   ├── login.html
│   ├── register.html
│   ├── student-dashboard.html
│   ├── dashboard.html
│   ├── css/
│   └── js/
├── sql/
│   ├── database_schema.sql
│   ├── register.sql
│   ├── sample_data.sql
│   └── reports.sql
└── tests/
```

## Setup on Windows

1. Install Python 3.10+ and MySQL 8.0+.
2. Open the project folder in VS Code.
3. Create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

4. Install the required packages:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

5. Copy `.env.example` to `.env` and enter your MySQL details. Set a long, random `SECRET_KEY`. Do not upload `.env` or share its contents.

## Database setup

### Fresh installation

Run these scripts in order from MySQL Workbench:

1. `sql/database_schema.sql`
2. `sql/sample_data.sql`

The schema creates all RPMS tables, including student registration fields and student login links.

### Existing RPMS database

Do not drop or recreate your existing database. Back it up first, then run `sql/register.sql` once to add the student registration fields and the `STUDENT` role.

The migration is for the database structure supplied with this project. If some of its ALTER statements have already been executed, inspect the table definitions before running it again.

## Start the application

From the project root:

```powershell
python main.py
```

Open:

- Login: `http://127.0.0.1:5000/login.html`
- Student registration: `http://127.0.0.1:5000/register.html`

Students can register, sign in using their email or mobile number, view their profile, browse open jobs and track their applications.

Staff sign in with username or email and select their role. The sample staff credentials are shown below.

## Demo staff login

| Role | Username | Password |
|---|---|---|
| ADMIN | admin | RPMS@123 |
| RECRUITER | recruiter1 | RPMS@123 |
| PLACEMENT_OFFICER | placement | RPMS@123 |

These credentials are for local demonstration only. Change them before using the application with real data.

## Tests

Run:

```powershell
pytest -q
```

The included unit tests cover application status transitions, candidate validation and eligibility rules. Database integration still requires a running MySQL server with the project schema loaded.

## Before real deployment

- Use a strong secret key and a least-privilege MySQL account.
- Change all demo passwords.
- Enable HTTPS and secure session cookies.
- Add CSRF protection, login rate limiting and a password reset process.
- Disable Flask debug mode and use a production WSGI server.
