#!/usr/bin/env python
"""
Initialize DyslexiaCheck with test account
Run this to create the demo test account
"""

from app import create_app, db
from app.models import User, LearningMaterial

app = create_app()

with app.app_context():
    # Create tables if they don't exist
    db.create_all()
    
    # Check if demo account exists
    demo_user = User.query.filter_by(username='demo').first()
    
    if not demo_user:
        print("Creating test account...")
        demo_user = User(
            username='demo',
            email='demo@test.com',
            age=25
        )
        demo_user.set_password('Demo123!')
        db.session.add(demo_user)
        db.session.commit()
        print("✓ Test account created!")
        print("  Username: demo")
        print("  Email: demo@test.com")
        print("  Password: Demo123!")
    else:
        print("✓ Test account already exists!")
        print("  Username: demo")
        print("  Password: Demo123!")
    
    # Check if learning materials exist
    materials_count = LearningMaterial.query.count()
    
    if materials_count == 0:
        print("\nAdding learning materials...")
        
        materials = [
            LearningMaterial(
                title='Phonics Fundamentals',
                category='Phonics',
                difficulty='beginner',
                description='Learn the basics of phonics and letter sounds',
                content='Phonics is the method of teaching reading and writing by emphasizing sound-symbol relationships. This foundational course covers the basics of how letters and letter combinations represent sounds in English.'
            ),
            LearningMaterial(
                title='Letter Sound Recognition',
                category='Phonics',
                difficulty='beginner',
                description='Master individual letter sounds',
                content='Each letter has specific sounds associated with it. This course teaches the phonetic value of each letter and helps develop automatic recognition of letter-sound relationships.'
            ),
            LearningMaterial(
                title='Sight Words Training',
                category='Sight Words',
                difficulty='beginner',
                description='Common words that need to be memorized',
                content='Sight words are common words that should be recognized automatically without sounding them out. These include words like "the", "and", "is", and many others that are essential for reading fluency.'
            ),
            LearningMaterial(
                title='Reading Comprehension Exercises',
                category='Reading',
                difficulty='intermediate',
                description='Improve your understanding of texts',
                content='Reading comprehension is the ability to process text and understand its meaning. This course provides exercises and strategies to improve your ability to understand and retain information from reading.'
            ),
            LearningMaterial(
                title='Vocabulary Building',
                category='Vocabulary',
                difficulty='intermediate',
                description='Expand your vocabulary',
                content='Building a strong vocabulary is essential for reading and communication. This course teaches strategies for learning new words and understanding their meanings in context.'
            ),
            LearningMaterial(
                title='Spelling Practice',
                category='Spelling',
                difficulty='intermediate',
                description='Master correct spelling',
                content='Proper spelling is important for clear written communication. This course provides practice with common spelling patterns, rules, and difficult words.'
            ),
            LearningMaterial(
                title='Reading Fluency',
                category='Reading',
                difficulty='intermediate',
                description='Read smoothly and naturally',
                content='Fluency is the ability to read quickly, accurately, and with expression. This course helps you develop faster reading speeds while maintaining comprehension.'
            ),
            LearningMaterial(
                title='Advanced Reading Materials',
                category='Reading',
                difficulty='advanced',
                description='Complex texts and literature',
                content='Advanced reading materials for proficient readers. These materials include complex sentence structures, sophisticated vocabulary, and challenging concepts.'
            ),
            LearningMaterial(
                title='Creative Writing',
                category='Writing',
                difficulty='advanced',
                description='Express yourself through writing',
                content='Creative writing allows for self-expression and imagination. This course teaches techniques for developing ideas, organizing thoughts, and expressing them effectively in writing.'
            ),
        ]
        
        for material in materials:
            db.session.add(material)
        
        db.session.commit()
        print("✓ 9 learning materials added!")
    else:
        print(f"\n✓ {materials_count} learning materials already exist!")
    
    print("\n✅ Database initialization complete!")
    print("\nYou can now login with:")
    print("  Username: demo")
    print("  Password: Demo123!")
