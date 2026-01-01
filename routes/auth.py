"""
routes/auth.py
--------------
Handles login using Flask sessions.
"""
#werkzeug security for password hashing
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from models import db


from flask import Blueprint, request, jsonify, session, redirect, url_for, render_template
from models import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=['GET'])
def login_page():
    """
    GET /auth/login
    Shows login page
    """
    return render_template('auth/login.html')


@auth_bp.route('/login', methods=['POST'])
def login():
    """
    POST /auth/login
    Authenticates user and creates session
    """

    email = request.form['email']
    password = request.form['password']

    user = User.query.filter_by(email=email).first()

    if not user:
        return render_template(
            'auth/login.html',
            error="Invalid email or password"
        )

    # check password hash
    if not check_password_hash(user.password_hash, password):
        return render_template(
            'auth/login.html',
            error="Invalid email or password"
        )

    # create session
    session['user_id'] = user.id
    session['role'] = user.role
    session['name'] = user.name
    session['email'] = user.email

    # redirect based on role
    if user.role == 'candidate':
        return redirect('/candidate/dashboard')
    elif user.role == 'admin':
        return redirect('/admin/dashboard')
    elif user.role == 'hr':
        return redirect('/hr/dashboard')

    return "Invalid role"


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    GET  /auth/signup  -> show signup form
    POST /auth/signup  -> create candidate user
    """

    if request.method == 'GET':
        return render_template('auth/signup.html')

    # POST request (form submitted)
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']

    # Check if email already exists
    existing_user = User.query.filter_by(email=email).first() #equivalent to SELECT * FROM users WHERE email = ? LIMIT 1;
    if existing_user:
        return render_template(
            'auth/signup.html',
            error="Email already registered"
        )

    # Hash the password automatically
    password_hash = generate_password_hash(password)

    # Create user with role = candidate
    user = User(
        role='candidate',
        name=name,
        email=email,
        phone=phone,
        password_hash=password_hash
    )

    db.session.add(user)
    db.session.commit()

    # Auto-login after signup
    session['user_id'] = user.id
    session['role'] = user.role
    session['name'] = user.name
    session['email'] = user.email

    # Redirect to candidate dashboard
    return redirect('/candidate/dashboard')



@auth_bp.route('/logout')
def logout():
    """
    GET /auth/logout
    Clears session
    """
    session.clear()
    return redirect('/auth/login')
