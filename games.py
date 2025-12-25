from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import GameScore
import random

games_bp = Blueprint('games', __name__, url_prefix='/games')

@games_bp.route('/')
@login_required
def index():
    return render_template('games_module.html')

@games_bp.route('/memory-match')
@login_required
def memory_match():
    return render_template('games/memory_match.html')

@games_bp.route('/word-puzzle')
@login_required
def word_puzzle():
    return render_template('games/word_puzzle.html')

@games_bp.route('/spelling-bee')
@login_required
def spelling_bee():
    return render_template('games/spelling_bee.html')

@games_bp.route('/typing-master')
@login_required
def typing_master():
    return render_template('games/typing_master.html')

@games_bp.route('/rhyme-match')
@login_required
def rhyme_match():
    return render_template('games/rhyme_match.html')

@games_bp.route('/sentence-builder')
@login_required
def sentence_builder():
    return render_template('games/sentence_builder.html')

@games_bp.route('/phonics-quest')
@login_required
def phonics_quest():
    return render_template('games/phonics_quest.html')

@games_bp.route('/save-score', methods=['POST'])
@login_required
def save_score():
    try:
        data = request.json
        
        # Validate required fields
        if not data.get('game_name'):
            return jsonify({'success': False, 'error': 'Game name is required'}), 400
        if data.get('score') is None:
            return jsonify({'success': False, 'error': 'Score is required'}), 400
        
        # Validate score is a number
        try:
            score = int(data.get('score', 0))
        except (TypeError, ValueError):
            return jsonify({'success': False, 'error': 'Score must be a number'}), 400
        
        # Create game score record
        game_score = GameScore(
            user_id=current_user.id,
            game_name=data.get('game_name'),
            score=score,
            time_taken=float(data.get('time_taken', 0)),
            difficulty=data.get('difficulty', 'medium'),
            completed=data.get('completed', False)
        )
        
        db.session.add(game_score)
        db.session.commit()
        
        print(f'✅ Score saved: {current_user.username} - {data.get("game_name")} - {score} points')
        
        return jsonify({
            'success': True, 
            'message': 'Score saved!',
            'score_id': game_score.id,
            'data': {
                'game_name': game_score.game_name,
                'score': game_score.score,
                'time_taken': game_score.time_taken,
                'difficulty': game_score.difficulty,
                'completed': game_score.completed,
                'created_at': game_score.created_at.isoformat()
            }
        })
    except Exception as e:
        print(f'❌ Error saving score: {str(e)}')
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 400

@games_bp.route('/scores')
@login_required
def scores():
    game_scores = GameScore.query.filter_by(user_id=current_user.id).order_by(
        GameScore.created_at.desc()
    ).all()
    return render_template('scoreboard.html', scores=game_scores)
