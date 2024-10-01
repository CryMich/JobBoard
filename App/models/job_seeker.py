from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

applied_jobs = db.Table('applied_jobs',
    db.Column('job_seeker_id', db.Integer, db.ForeignKey('job_seeker.jobseeker_id'), primary_key=True),
    db.Column('job_posting_id', db.Integer, db.ForeignKey('job_postings.jobId'), primary_key=True)
)

class JobSeeker(db.Model):
    jobseeker_id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    user_type = db.Column(db.String(20), nullable=False)

    applied_jobs = db.relationship('JobPostings', secondary='applied_jobs', backref='applicants')

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        self.user_type = 'JobSeeker'

    def get_json(self):
        return{
            'jobseeker_id': self.jobseeker_id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

