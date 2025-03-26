
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# Initialize Flask App
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skill_gap_analyzer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db = SQLAlchemy(app)

# Define Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    skills = db.Column(db.String(500), nullable=False)  # Comma-separated skills

class JobRequirement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    required_skills = db.Column(db.String(500), nullable=False)  # Comma-separated skills

# Create Database Tables
with app.app_context():
    db.create_all()

# API Routes
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(name=data['name'], skills=data['skills'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully!'})

@app.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{'id': u.id, 'name': u.name, 'skills': u.skills} for u in users]
    return jsonify(users_list)

@app.route('/add_job', methods=['POST'])
def add_job():
    data = request.json
    new_job = JobRequirement(title=data['title'], required_skills=data['required_skills'])
    db.session.add(new_job)
    db.session.commit()
    return jsonify({'message': 'Job added successfully!'})

@app.route('/get_jobs', methods=['GET'])
def get_jobs():
    jobs = JobRequirement.query.all()
    jobs_list = [{'id': j.id, 'title': j.title, 'required_skills': j.required_skills} for j in jobs]
    return jsonify(jobs_list)

# AI Model Integration (Dummy Skill Gap Analysis)
@app.route('/analyze_skill_gap', methods=['POST'])
def analyze_skill_gap():
    data = request.json
    user_skills = set(data['skills'].split(','))
    job_id = data['job_id']
    
    job = JobRequirement.query.get(job_id)
    if not job:
        return jsonify({'error': 'Job not found'}), 404

    required_skills = set(job.required_skills.split(','))

    missing_skills = required_skills - user_skills

    return jsonify({
        'job_title': job.title,
        'missing_skills': list(missing_skills),
        'message': 'Skill gap analysis completed!'
    })

# Run the Flask App
if __name__== '_main_':
    app.run(debug=True)


       
