# API Endpoints Reference

## Authentication Routes (`/auth`)

### POST `/auth/signup`
Create new user account
```json
{
  "username": "string",
  "email": "string@example.com",
  "password": "string",
  "age": "integer"
}
```
Returns: Redirect to dashboard

### POST `/auth/login`
Login to existing account
```json
{
  "username": "string",
  "password": "string"
}
```
Returns: Redirect to dashboard

### GET `/auth/logout`
Logout current user
Returns: Redirect to login

---

## Main Routes (`/main`)

### GET `/`
Homepage (redirects to dashboard if logged in)

### GET `/home`
Home page (redirects to dashboard if logged in)

### GET `/dashboard`
User dashboard with statistics
Returns: Dashboard template with:
- `recent_scores` - Last 5 game scores
- `recent_tests` - Last 5 dyslexia tests
- `learning_progress` - All learning progress
- `avg_score` - Average game score

### GET `/about`
About page

### GET `/services`
Services page

### GET `/contact`
Contact page

---

## Dyslexia Routes (`/dyslexia`)

### GET `/dyslexia/`
Dyslexia checker main page
Returns: dyslexia_checker.html template

### POST `/dyslexia/handwriting`
Analyze handwriting from canvas drawing
```json
{
  "image": "data:image/png;base64,..."
}
```
Returns:
```json
{
  "success": true,
  "probability": 65.5,
  "risk_level": "medium",
  "analysis": {
    "letter_spacing": 0.8,
    "line_alignment": 0.9,
    "letter_consistency": 0.75,
    "pressure_variation": 0.7,
    "slant_consistency": 0.85
  },
  "recommendations": [
    {"id": 1, "title": "Material Name", "category": "Category"}
  ]
}
```

### POST `/dyslexia/speech`
Analyze speech from audio recording
```json
{
  "audio": "audio_data_placeholder"
}
```
Returns:
```json
{
  "success": true,
  "probability": 45.2,
  "risk_level": "low",
  "analysis": {
    "speech_rate": 0.9,
    "pronunciation_clarity": 0.85,
    "word_repetition": 0.7,
    "hesitation_frequency": 0.8,
    "phoneme_accuracy": 0.88
  },
  "recommendations": [...]
}
```

### GET `/dyslexia/history`
View all dyslexia tests for current user
Returns: dyslexia_history.html template with `tests` list

---

## Games Routes (`/games`)

### GET `/games/`
Games hub - select game to play
Returns: games_module.html template

### GET `/games/memory-match`
Memory Match game
Returns: games/memory_match.html

### GET `/games/word-puzzle`
Word Puzzle game
Returns: games/word_puzzle.html

### GET `/games/spelling-bee`
Spelling Bee game
Returns: games/spelling_bee.html

### GET `/games/typing-master`
Typing Master game
Returns: games/typing_master.html

### GET `/games/rhyme-match`
Rhyme Match game
Returns: games/rhyme_match.html

### GET `/games/sentence-builder`
Sentence Builder game
Returns: games/sentence_builder.html

### GET `/games/phonics-quest`
Phonics Quest game
Returns: games/phonics_quest.html

### POST `/games/save-score`
Save game score
```json
{
  "game_name": "Memory Match",
  "score": 85,
  "time_taken": 120,
  "difficulty": "medium",
  "completed": true
}
```
Returns:
```json
{
  "success": true,
  "message": "Score saved!"
}
```

### GET `/games/scores`
View scoreboard with all game scores
Returns: scoreboard.html template with:
- `scores` - All game scores for user
- Statistics calculated from scores

---

## Learning Routes (`/learning`)

### GET `/learning/`
View all learning materials
Returns: learning_materials.html template with:
- `materials` - List of 9 materials

### GET `/learning/material/<material_id>`
View single material details
Returns: JSON with material data

### POST `/learning/start/<material_id>`
Start learning a material
```json
{}
```
Returns:
```json
{
  "success": true,
  "progress_id": 123
}
```

### POST `/learning/update-progress/<material_id>`
Update learning progress
```json
{
  "progress_percentage": 50
}
```
Returns:
```json
{
  "success": true
}
```

### GET `/learning/progress`
View user's learning progress
Returns: progress data for all materials

---

## Dashboard Routes (`/dashboard`)

### GET `/dashboard/`
Main dashboard (same as `/dashboard`)
Returns: Aggregated user statistics

---

## Database Models

### User
- id (Integer)
- username (String, unique)
- email (String, unique)
- password_hash (String)
- age (Integer)
- created_at (DateTime)

### DyslexiaTest
- id (Integer)
- user_id (ForeignKey)
- test_type (String) - 'handwriting' or 'speech'
- analysis_results (JSON)
- dyslexia_probability (Float) - 0-100
- risk_level (String) - 'low', 'medium', 'high'
- recommendations (JSON)
- test_data (String) - Base64 encoded
- created_at (DateTime)

### GameScore
- id (Integer)
- user_id (ForeignKey)
- game_name (String)
- score (Integer)
- time_taken (Integer) - seconds
- difficulty (String) - 'easy', 'medium', 'hard'
- completed (Boolean)
- created_at (DateTime)

### LearningProgress
- id (Integer)
- user_id (ForeignKey)
- material_id (Integer)
- category (String)
- progress_percentage (Integer) - 0-100
- completed (Boolean)
- started_at (DateTime)
- completed_at (DateTime)

### LearningMaterial
- id (Integer)
- title (String)
- category (String)
- description (String)
- content (String)
- difficulty (String) - 'beginner', 'intermediate', 'advanced'
- video_url (String)
- resource_url (String)
- created_at (DateTime)

---

## Status Codes

- **200** - Success
- **201** - Created
- **400** - Bad Request
- **401** - Unauthorized
- **404** - Not Found
- **500** - Server Error

---

## Authentication

All protected endpoints require:
- User to be logged in (via Flask-Login)
- Valid session cookie

Protected routes are marked with `@login_required` decorator

---

## Data Formats

### Difficulty Levels
- `beginner` - Easier content
- `intermediate` - Medium difficulty
- `advanced` - Challenging content

### Risk Levels
- `low` - Probability < 40%
- `medium` - Probability 40-70%
- `high` - Probability > 70%

### Game Difficulties
- `easy` - Easier gameplay
- `medium` - Standard difficulty
- `hard` - Challenging gameplay

### Test Types
- `handwriting` - Canvas drawing analysis
- `speech` - Audio recording analysis

---

## Common Response Patterns

### Success Response
```json
{
  "success": true,
  "data": {...}
}
```

### Error Response
```json
{
  "success": false,
  "error": "Error message"
}
```

---

## Rate Limiting

No rate limiting currently implemented.
Suitable for single-user or small team use.

---

## CORS

CORS is not enabled. Access must be from same origin.
For production, configure CORS as needed.

---

## Examples

### Save Game Score
```bash
curl -X POST http://localhost:5000/games/save-score \
  -H "Content-Type: application/json" \
  -d '{
    "game_name": "Memory Match",
    "score": 85,
    "time_taken": 120,
    "difficulty": "medium",
    "completed": true
  }'
```

### Get Scoreboard
```bash
curl http://localhost:5000/games/scores
```

### Get Learning Materials
```bash
curl http://localhost:5000/learning/
```

---

*Reference Created: November 13, 2025*
*API Version: 1.0*
