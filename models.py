from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    dyslexia_tests = db.relationship('DyslexiaTest', backref='user', lazy=True, cascade='all, delete-orphan')
    game_scores = db.relationship('GameScore', backref='user', lazy=True, cascade='all, delete-orphan')
    learning_progress = db.relationship('LearningProgress', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_average_score(self):
        if self.game_scores:
            return sum(score.score for score in self.game_scores) / len(self.game_scores)
        return 0

class DyslexiaTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    test_type = db.Column(db.String(50), nullable=False)  # 'handwriting' or 'speech'
    analysis_results = db.Column(db.JSON, nullable=False)
    dyslexia_probability = db.Column(db.Float)  # 0-100 percentage
    risk_level = db.Column(db.String(20))  # 'low', 'medium', 'high'
    recommendations = db.Column(db.JSON)  # Array of recommended learning materials
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    test_data = db.Column(db.LargeBinary)  # Store image/audio data

class GameScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    game_name = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, default=0)
    time_taken = db.Column(db.Float)  # in seconds
    difficulty = db.Column(db.String(20))  # 'easy', 'medium', 'hard'
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class LearningProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    material_id = db.Column(db.String(100))
    material_title = db.Column(db.String(200))
    category = db.Column(db.String(100))  # 'phonics', 'sight-words', 'comprehension', etc.
    progress_percentage = db.Column(db.Float, default=0)
    completed = db.Column(db.Boolean, default=False)
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)

class LearningMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100))
    description = db.Column(db.Text)
    content = db.Column(db.Text)
    difficulty = db.Column(db.String(20))  # 'beginner', 'intermediate', 'advanced'
    video_url = db.Column(db.String(255))
    resource_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
