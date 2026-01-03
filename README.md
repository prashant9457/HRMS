Landing Page (/)
│
├─ Signup
│   └─ Create User (role: candidate / admin / hr)
│
└─ Login
    └─ Session Created
        └─ Redirect based on role

Candidate Dashboard
│
├─ View Profile
│   └─ Complete / Update Candidate Profile   (applied)
│
├─ Job Feed
│   ├─ Filter Jobs (dept, location, role)
│   ├─ View Job Details
│   └─ Apply for Job
│       └─ Application Status = applied
│
└─ My Applications
    └─ Track Status
        ├─ applied
        ├─ shortlisted (future)
        ├─ selected
        └─ rejected

Recruitment Admin Dashboard
│
├─ Create Job
│   └─ Publish Job
│
├─ View Jobs
│   └─ View Applicants (per job)
│       ├─ Review Candidate Details
│       └─ Shortlist for Interview
│           └─ Application Status = shortlisted
│
└─ Recruitment Reports (future)
    ├─ No. of applicants
    ├─ Dept-wise hiring
    └─ Vacancy tracking

HR Dashboard
│
├─ View Shortlisted Candidates
│   ├─ Conduct Interview
│   ├─ Verify Documents
│   └─ Final Decision
│       ├─ Select
│       │   └─ Application Status = selected
│       │       └─ Create Employee Record
│       │           └─ Employee Lifecycle Starts
│       │
│       └─ Reject
│           └─ Application Status = rejected
│
└─ Employee Management (future)
    ├─ Attendance
    ├─ Transfers
    ├─ Payroll
    ├─ Performance
    └─ Grievances
