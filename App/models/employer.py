from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Employer(db.Model):
    employer_id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    user_type = db.Column(db.String(20), nullable=False)
    companyId = db.Column(db.Integer, unique=True, nullable=False)
    companyName = db.Column(db.String(120), nullable=False)

    jobs_posted = db.relationship('JobPostings', backref='employer', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        self.user_type = 'Employer'

    def get_json(self):
        return {
            'employer_id': self.employer_id,
            'username': self.username,
            'companyId': self.companyId,
            'companyName': self.companyName
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)