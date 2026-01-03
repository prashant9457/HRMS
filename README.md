🏛️ HRMS Platform – Municipal Corporation of Delhi (MCD)

A centralized Human Resource Management System (HRMS) prototype designed for the Municipal Corporation of Delhi (MCD) to streamline recruitment, onboarding, and employee lifecycle management at scale.

This project demonstrates a role-based, workflow-driven HRMS architecture aligned with real municipal operations.

📌 Problem Statement

How can a unified Human Resource Management System (HRMS) be designed for the Municipal Corporation of Delhi to efficiently manage recruitment, attendance, transfers, payroll, performance tracking, grievance redressal, and inter-department coordination across thousands of municipal employees?

🧠 Solution Overview

This HRMS prototype is built around a centralized core that connects multiple stakeholders through role-based dashboards and a modular service layer.

The system separates recruitment, HR operations, and employee lifecycle management, ensuring transparency, scalability, and governance-friendly workflows.

🏗️ System Architecture (High Level)

Central HRMS Core

Authentication & role-based access control

Workflow orchestration

Centralized business logic

Role-Based Access

Candidate

Recruitment Admin

HR

Employee (future scope)

Modular Service Layer

Recruitment & Onboarding

Attendance (planned)

Payroll (planned)

Grievance & Performance (planned)

👥 User Roles & Responsibilities
🟢 Candidate

Sign up and log in securely

Create and manage candidate profile

Browse job listings

Apply for jobs

Track application status (applied → shortlisted → selected/rejected)

🟠 Recruitment Admin

Create and publish job postings

View applicants for each job

Review candidate details

Shortlist candidates for interview

Recruitment Admin handles screening and shortlisting only.

🔴 HR (Human Resources)

View shortlisted candidates

Conduct interviews

Final selection or rejection

Onboard selected candidates

Convert candidate data into employee records (no re-entry)

HR manages interview, onboarding, and post-selection workflows.

🔄 Recruitment Workflow
Candidate applies for job
↓
Recruitment Admin shortlists candidate
↓
HR conducts interview
↓
HR selects or rejects
↓
If selected → Employee onboarding


The system follows a status-driven workflow to ensure auditability and transparency.

🔐 Authentication & Security

Secure login and signup

Passwords are never stored in plain text

All passwords are stored using secure hashing algorithms

Session-based authentication

Role-based access control (RBAC)

Even admins cannot view user passwords.

🧪 Demo Credentials (For Prototype Testing)
🔸 Recruitment Admin
Email: admin@mcd.in
Password: password123

🔸 Candidate
Email: 1abhishekpandey2@gmail.com
Password: 1234

🔸 HR
Email: hari@hr.in
Password: hari


⚠️ These credentials are for demo/testing purposes only.

🖥️ Key Features Implemented

User signup & login

Role-based dashboards

Job creation and publishing

Job application system

Candidate profile management

Application tracking

Admin shortlisting workflow

HR interview & onboarding workflow

Secure session handling

Clean modular project structure

🚀 Future Scope

Attendance management (biometric / GPS-based)

Payroll processing

Performance evaluation

Grievance redressal system

Transfer & posting management

Analytics & reporting dashboards

AI-assisted recruitment screening

🛠️ Tech Stack

Backend: Python, Flask

Database: SQLite (Prototype)

ORM: SQLAlchemy

Authentication: Flask Sessions, Werkzeug Security

Frontend: HTML, CSS (Server-rendered templates)

📂 Project Structure (Simplified)
hrms/
├── app.py
├── models.py
├── routes/
│   ├── auth.py
│   ├── candidate.py
│   ├── admin.py
│   └── hr.py
├── templates/
│   ├── candidate/
│   ├── admin/
│   └── hr/
├── static/
│   └── css/
└── instance/
    └── database.db

🎯 Why This Design Works for MCD

Mirrors real municipal workflows

Clear separation of responsibilities

Scales across departments

Audit-friendly and transparent

Easy to extend with new services

🏁 Conclusion

This HRMS prototype demonstrates how a centralized, role-based, modular architecture can digitize and streamline HR operations for a large municipal body like MCD, while remaining scalable, secure, and governance-ready.
