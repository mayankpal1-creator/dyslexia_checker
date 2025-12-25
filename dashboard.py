from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import GameScore, DyslexiaTest, LearningProgress

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
@login_required
def index():
    recent_scores = GameScore.query.filter_by(user_id=current_user.id).order_by(
        GameScore.created_at.desc()
    ).limit(5).all()
    
    recent_tests = DyslexiaTest.query.filter_by(user_id=current_user.id).order_by(
        DyslexiaTest.created_at.desc()
    ).limit(5).all()
    
    learning_progress = LearningProgress.query.filter_by(user_id=current_user.id).all()
    
    avg_score = current_user.get_average_score()
    
    return render_template(
        'dashboard.html',
        recent_scores=recent_scores,
        recent_tests=recent_tests,
        learning_progress=learning_progress,
        avg_score=avg_score
    )
