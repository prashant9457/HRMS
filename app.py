"""
app.py
------
This is the ENTRY POINT of the HRMS application.

Responsibilities:
- Create Flask app
- Configure database
- Register all route blueprints
- Run the server

NOTE:
No business logic should be written here.
"""

from flask import Flask,session, redirect, render_template
from models import db

# Import route blueprints
# Each blueprint contains routes for a specific role
from routes.auth import auth_bp
from routes.candidate import candidate_bp
from routes.admin import admin_bp
from routes.hr import hr_bp

# Create Flask application
app = Flask(__name__)

# Database configuration (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Secret key (used later for sessions/auth)
app.config['SECRET_KEY'] = 'dev-secret-key'

# Attach database to this Flask app
db.init_app(app)

# Register blueprints (connect routes to app)
app.register_blueprint(auth_bp)
app.register_blueprint(candidate_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(hr_bp)

# Basic home route (health check)


@app.route('/')
def home():
    """
    Public landing page.
    If user is already logged in, redirect to their dashboard.
    """

    if 'user_id' in session:
        role = session.get('role')

        if role == 'candidate':
            return redirect('/candidate/dashboard')
        elif role == 'admin':
            return redirect('/admin/dashboard')
        elif role == 'hr':
            return redirect('/hr/dashboard')

    # Not logged in → show landing page
    return render_template('landing.html')


# Start the server
if __name__ == '__main__':
    app.run(debug=True)
