from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from app.models import GameScore, DyslexiaTest, LearningProgress
from app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('index.html')

@main_bp.route('/home')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('home.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    recent_scores = GameScore.query.filter_by(user_id=current_user.id).order_by(
        GameScore.created_at.desc()
    ).limit(5).all()
    
    recent_tests = DyslexiaTest.query.filter_by(user_id=current_user.id).order_by(
        DyslexiaTest.created_at.desc()
    ).limit(5).all()
    
    learning_progress = LearningProgress.query.filter_by(user_id=current_user.id).all()
    
    # Calculate average score
    avg_score = 0
    if recent_scores:
        avg_score = sum(s.score for s in recent_scores) / len(recent_scores)
    
    return render_template(
        'dashboard.html',
        recent_scores=recent_scores,
        recent_tests=recent_tests,
        learning_progress=learning_progress,
        avg_score=avg_score
    )

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/services')
def services():
    return render_template('services.html')

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')
