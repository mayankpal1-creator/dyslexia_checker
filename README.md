# DyslexiaCheck README

## Overview
DyslexiaCheck is a comprehensive web-based platform for early detection of dyslexia and providing personalized learning support. The application uses advanced handwriting and speech analysis to identify potential dyslexia indicators and recommends appropriate learning materials.

## Features

### 1. **Dyslexia Checker**
- Handwriting analysis with letter spacing, slant, and pressure evaluation
- Speech analysis examining pronunciation and phonetic accuracy
- Risk probability scoring and detailed metrics
- Personalized recommendations based on test results

### 2. **Learning Materials**
- Curated educational resources organized by difficulty level
- Categories include:
  - Phonics and sound recognition
  - Sight words training
  - Reading comprehension
  - Vocabulary building
  - Spelling practice
  - Reading fluency
  - Creative writing

### 3. **Interactive Games** (7 games included)
1. **Memory Match** - Enhance memory and visual recognition
2. **Word Puzzle** - Build vocabulary and problem-solving skills
3. **Spelling Bee** - Practice correct spelling
4. **Typing Master** - Improve typing speed and accuracy
5. **Rhyme Match** - Develop phonetic awareness
6. **Sentence Builder** - Learn grammar and sentence construction
7. **Phonics Quest** - Master phonetic sounds

### 4. **Progress Tracking**
- Detailed score tracking for all games
- Learning material progress monitoring
- Scoreboard with game statistics
- Performance analytics and trends

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Steps

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python run.py
   ```

5. **Access the application:**
   Open your browser and go to `http://localhost:5000`

## Project Structure

```
dyslexia/
├── app/
│   ├── __init__.py           # Flask app initialization
│   ├── models.py             # Database models
│   ├── routes/
│   │   ├── auth.py           # Authentication routes
│   │   ├── main.py           # Main routes
│   │   ├── dyslexia.py       # Dyslexia checker routes
│   │   ├── games.py          # Games routes
│   │   ├── learning.py       # Learning materials routes
│   │   └── dashboard.py      # Dashboard routes
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css     # Main stylesheet
│   │   ├── js/
│   │   │   └── main.js       # Main JavaScript
│   │   └── data/             # Static data files
│   └── templates/
│       ├── base.html         # Base template
│       ├── index.html        # Home page
│       ├── login.html        # Login page
│       ├── signup.html       # Sign up page
│       ├── dashboard.html    # User dashboard
│       ├── dyslexia_checker.html
│       ├── learning_materials.html
│       ├── games_module.html
│       ├── scoreboard.html
│       └── games/            # Individual game templates
├── config.py                 # Configuration settings
├── requirements.txt          # Python dependencies
├── run.py                    # Application entry point
└── README.md                 # This file
```

## Usage

### For New Users
1. Click "Sign Up" to create an account
2. Provide username, email, password, and age
3. Log in with your credentials

### For Taking Tests
1. Navigate to "Dyslexia Checker"
2. Choose between handwriting or speech analysis
3. Follow the instructions to complete the test
4. View detailed results and recommendations

### For Learning
1. Go to "Learning Materials"
2. Browse materials by category or difficulty
3. Click "Start Learning" to begin
4. Track your progress

### For Games
1. Access "Games" section
2. Choose a game to play
3. Try to achieve the highest score
4. View scores on the Scoreboard

## Technology Stack

### Backend
- **Framework:** Flask 2.3.2
- **Database:** SQLAlchemy with SQLite
- **Authentication:** Flask-Login with password hashing
- **ORM:** SQLAlchemy 2.0

### Frontend
- **HTML5:** Semantic markup
- **CSS3:** Modern styling with CSS Grid and Flexbox
- **JavaScript:** Interactive features and games
- **Canvas API:** Drawing functionality for handwriting analysis

### Analysis
- **Handwriting Analysis:** Canvas-based image processing
- **Speech Analysis:** Web Speech API integration
- **Data Processing:** NumPy and Scikit-learn (optional)

## Database Schema

### User Model
- id, username, email, password_hash, age, created_at
- Relationships: dyslexia_tests, game_scores, learning_progress

### DyslexiaTest Model
- id, user_id, test_type, analysis_results, dyslexia_probability
- risk_level, recommendations, created_at

### GameScore Model
- id, user_id, game_name, score, time_taken
- difficulty, completed, created_at

### LearningProgress Model
- id, user_id, material_id, category, progress_percentage
- completed, started_at, completed_at

## Configuration

Edit `config.py` to customize:
- Secret key (for production)
- Database URI
- Upload settings
- Session timeout
- File size limits

## Security Notes

⚠️ **Important for Production:**
1. Change the SECRET_KEY in config.py
2. Set DEBUG = False
3. Use a production database (PostgreSQL recommended)
4. Enable HTTPS
5. Configure CSRF protection
6. Implement rate limiting
7. Add CORS headers as needed

## API Endpoints

### Authentication
- `POST /login` - User login
- `POST /signup` - User registration
- `GET /logout` - User logout

### Dyslexia Testing
- `POST /dyslexia/handwriting` - Analyze handwriting
- `POST /dyslexia/speech` - Analyze speech
- `GET /dyslexia/history` - View test history

### Games
- `GET /games/` - Games list
- `POST /games/save-score` - Save game score
- `GET /games/scores` - View scoreboard

### Learning
- `GET /learning/` - Learning materials
- `POST /learning/start/<id>` - Start material
- `POST /learning/update-progress/<id>` - Update progress

## Troubleshooting

### Application won't start
- Check that port 5000 is available
- Ensure all dependencies are installed
- Check Python version compatibility

### Database errors
- Delete `dyslexia.db` and restart to create a fresh database
- Check database file permissions

### Games not working
- Ensure JavaScript is enabled
- Check browser console for errors
- Try a different browser

## Future Enhancements

- Machine learning models for improved accuracy
- Mobile app version
- Multi-language support
- Advanced analytics dashboard
- Parent/teacher reporting features
- Integration with educational platforms
- Video tutorials and guided learning paths
- Community forums and support

## Support & Feedback

For issues, suggestions, or contributions:
- Check the FAQ in the Contact page
- Review existing documentation
- Contact support through the application

## License

This project is provided as-is for educational purposes.

## Credits

Created with ❤️ for supporting individuals with dyslexia.

---

**Happy Learning! 📚**
