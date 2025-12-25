#!/usr/bin/env python
"""Create test account for DyslexiaCheck"""
from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    db.create_all()
    
    # Check if demo exists
    if not User.query.filter_by(username='demo').first():
        user = User(username='demo', email='demo@test.com', age=25)
        user.set_password('Demo123!')
        db.session.add(user)
        db.session.commit()
        print('✓ Test account created: demo / Demo123!')
    else:
        print('✓ Test account already exists: demo / Demo123!')
