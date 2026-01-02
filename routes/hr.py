"""
routes/hr.py
------------
Routes for HR admins.
"""

from flask import Blueprint, request, jsonify, render_template, session, redirect
from models import db, Employee, CandidateProfile, Transfer



hr_bp = Blueprint('hr', __name__, url_prefix='/hr')


@hr_bp.route('/dashboard')
def hr_dashboard():
    """
    HR dashboard
    """
    if 'user_id' not in session or session.get('role') != 'HR':
        return redirect('/auth/login')

    return render_template(
        'hr/dashboard.html',
        user=session
    )



@hr_bp.route('/ui/create-employee')
def create_employee_ui():
    return render_template('hr/create_employee.html')


@hr_bp.route('/create-employee', methods=['POST'])
def create_employee():
    """
    POST /hr/create-employee

    Converts selected candidate into employee.
    """
    data = request.json

    candidate = CandidateProfile.query.get(data['candidate_id'])
    if not candidate:
        return jsonify({"error": "Candidate not found"}), 404

    employee = Employee(
        user_id=candidate.user_id,
        employee_code=data['employee_code'],
        department=data['department'],
        designation=data['designation'],
        pay_grade=data['pay_grade'],
        date_of_joining=data['date_of_joining'],
        status='active'
    )

    db.session.add(employee)
    db.session.commit()

    return jsonify({"message": "Employee created without re-entry"})


@hr_bp.route('/transfer', methods=['POST'])
def transfer_employee():
    """
    POST /hr/transfer

    Handles employee transfer between departments or locations.

    Flow:
    1. Validate employee exists
    2. Insert transfer record (history)
    3. Update employee's CURRENT department/location
    """

    data = request.json

    # Step 1: Fetch employee
    employee = Employee.query.get(data['employee_id'])
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    # Step 2: Create transfer record (history)
    transfer = Transfer(
        employee_id=employee.id,
        from_department=employee.department,
        from_location=data.get('from_location'),

        to_department=data['to_department'],
        to_location=data.get('to_location'),

        effective_date=data['effective_date'],
        order_number=data.get('order_number'),
        reason=data.get('reason')
    )

    db.session.add(transfer)

    # Step 3: Update employee's current posting
    employee.department = data['to_department']

    db.session.commit()

    return jsonify({
        "message": "Employee transferred successfully",
        "employee_id": employee.id
    })
