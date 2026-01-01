"""
routes/candidate.py
-------------------
Routes accessible by candidates.
"""

from flask import Blueprint, request, jsonify, render_template, session, redirect
from models import db, Application, Job

candidate_bp = Blueprint('candidate', __name__, url_prefix='/candidate')



@candidate_bp.route('/jobs')
def list_jobs():
    """
    GET /candidate/jobs

    This route is used by the CANDIDATE DASHBOARD
    to fetch all PUBLISHED jobs.

    It also supports filters like:
    - department
    - location
    """

    # Read filter values from URL query params
    # Example:
    # /candidate/jobs?department=Health&location=Zone A
    department = request.args.get('department')
    location = request.args.get('location')

    # Start with only OPEN (published) jobs
    query = Job.query.filter_by(status='open')

    # Apply department filter if provided
    if department:
        query = query.filter(Job.department.ilike(f"%{department}%")) #SELECT * FROM job WHERE department ILIKE '%value%';


    # Apply location filter if provided
    if location:
        query = query.filter(Job.location.ilike(f"%{location}%"))

    # Fetch final job list from DB
    jobs = query.all()

    # Convert DB objects into JSON-friendly format
    job_list = []
    for job in jobs:
        job_list.append({
            "id": job.id,                 # hidden from user, used internally
            "title": job.title,
            "department": job.department,
            "location": job.location,
            "vacancies": job.vacancies
        })

    # Return job list to frontend
    return jsonify(job_list)





@candidate_bp.route('/dashboard')
def candidate_dashboard():
    """
    Candidate dashboard
    """
    if 'user_id' not in session or session.get('role') != 'candidate':
        return redirect('/auth/login')

    return render_template(
        'candidate/dashboard.html',
        user=session
    )




@candidate_bp.route('/ui/apply')
def apply_ui():
    return render_template('candidate/apply.html')




@candidate_bp.route('/apply', methods=['POST'])
def apply_job():
    """
    POST /candidate/apply

    Candidate applies for a job.
    """
    data = request.json

    application = Application(
        candidate_id=data['candidate_id'],
        job_id=data['job_id'],
        status='applied'
    )

    db.session.add(application)
    db.session.commit()

    return jsonify({"message": "Application submitted"})
