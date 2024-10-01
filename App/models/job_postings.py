from App.database import db

class JobPostings(db.Model):
    jobId = db.Column(db.Integer, primary_key=True)
    jobTitle = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    salary = db.Column(db.Float)
    status = db.Column(db.String(50), nullable=False) #open or closed

    employer_id = db.Column(db.Integer, db.ForeignKey('employer.employer_id'))
