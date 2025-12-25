# DyslexiaCheck - Complete Testing Guide

This guide helps you test all features of the DyslexiaCheck platform.

## Quick Start

1. **Start the application:**
   ```
   python run.py
   ```
   Or double-click `start.bat` on Windows

2. **Open browser:**
   ```
   http://localhost:5000
   ```

3. **Create/Login to account:**
   - Use demo/Demo123! or create your own

---

## Feature Testing Checklist

### 1. ✍️ Dyslexia Checker - Handwriting Analysis

**How to test:**
1. Go to Dashboard → "Dyslexia Checker" card
2. Click on "Handwriting Analysis"
3. Draw in the canvas (write some letters/words)
4. Click "Analyze"

**Expected Results:**
- ✅ Drawing appears on canvas
- ✅ Analysis shows probability percentage (0-100%)
- ✅ Risk level displayed (HIGH/MEDIUM/LOW)
- ✅ Metrics shown: letter_spacing, line_alignment, letter_consistency, pressure_variation, slant_consistency
- ✅ Recommended learning materials displayed
- ✅ Result saved to database (visible in test history)

**Verify in Database:**
- Go to "View Test History" link
- Check "Handwriting" tests appear
- Click test to see all details

---

### 2. 🎤 Dyslexia Checker - Speech Analysis

**How to test:**
1. Go to Dashboard → "Dyslexia Checker" card
2. Click on "Speech Analysis"
3. Click "Start Recording"
4. Read the passage: "Reading is an important skill..."
5. Click "Stop Recording"

**Expected Results:**
- ✅ Microphone permission prompt appears
- ✅ Recording button changes to stop button
- ✅ Analysis shows probability percentage
- ✅ Risk level displayed (HIGH/MEDIUM/LOW)
- ✅ Metrics shown: speech_rate, pronunciation_clarity, word_repetition, hesitation_frequency, phoneme_accuracy
- ✅ Result saved to database

**Verify in Database:**
- Go to "View Test History"
- Check "Speech" tests appear

---

### 3. 🎮 Games - Score Saving

#### 3.1 Memory Match Game

**How to test:**
1. Go to Dashboard → "Games" card
2. Select "Memory Match"
3. Click cards to find matching pairs
4. Complete the game (find all 8 pairs)
5. Click "Save Score" button

**Expected Results:**
- ✅ Cards flip when clicked
- ✅ Matching pairs stay revealed
- ✅ Non-matching pairs flip back
- ✅ Score calculated (100 - moves*2)
- ✅ Completion time tracked
- ✅ "Score saved!" message appears
- ✅ Score saved to database

**Verify Scores:**
1. Go to Dashboard → "Scoreboard" card
2. Check "Memory Match" appears in the table
3. Score, time, and difficulty displayed

#### 3.2 Other Games

**Games to test:** (same flow as Memory Match)
- 🔤 Word Puzzle
- 🐝 Spelling Bee
- ⌨️ Typing Master
- 🎵 Rhyme Match
- 📝 Sentence Builder
- 🎯 Phonics Quest

**For each game:**
1. Play the game
2. Click "Save Score" button
3. Verify score appears in Scoreboard

---

### 4. 📊 Scoreboard - View Saved Scores

**How to test:**
1. Go to Dashboard → "Scoreboard" card (or Games → View Scores)
2. Check statistics at top:
   - Total Score (sum of all scores)
   - Games Played (count of games)
   - Average Score (mean of all scores)
   - Completed (count of completed games)

**Expected Results:**
- ✅ All game scores listed in table
- ✅ Games sorted by most recent first
- ✅ Columns: Game name, Score, Time, Difficulty, Status, Date
- ✅ Statistics cards show correct totals
- ✅ Color-coded difficulty badges (green=easy, yellow=medium, red=hard)

**Sample Data:**
- After playing 3 games, should show 3 rows
- Average score should calculate correctly
- Total score should be sum of all scores

---

### 5. 📚 Learning Materials - Display & Start

**How to test:**
1. Go to Dashboard → "Learning Materials" card
2. See 9 materials displayed:
   - Phonics Fundamentals (Beginner)
   - Letter Sound Recognition (Beginner)
   - Sight Words Training (Beginner)
   - Reading Comprehension Exercises (Intermediate)
   - Vocabulary Building (Intermediate)
   - Spelling Practice (Intermediate)
   - Reading Fluency (Intermediate)
   - Advanced Reading Materials (Advanced)
   - Creative Writing (Advanced)

**Expected Results:**
- ✅ All 9 materials visible
- ✅ Difficulty badges show correct levels:
  - Green = Beginner
  - Yellow = Intermediate
  - Red = Advanced
- ✅ Categories displayed: Phonics, Sight Words, Reading, Vocabulary, Spelling, Writing
- ✅ Click "Start Learning" to begin
- ✅ Material detail modal opens
- ✅ Progress tracked in database

**Material Details:**
Each material should have:
- Title ✓
- Category ✓
- Difficulty ✓
- Description ✓
- Content ✓

---

### 6. 📈 Dashboard - Statistics

**How to test:**
1. Go to Dashboard
2. Check statistics section:
   - Average Score
   - Total Games Played
   - Tests Completed
   - Learning Progress

**Expected Results:**
- ✅ Shows correct values based on user's data
- ✅ Updates after playing games/taking tests
- ✅ Color-coded cards (blue, green, cyan, pink)

---

### 7. 🔐 Authentication

**How to test:**
1. **Signup:** Create new account with email, password, age
2. **Login:** Login with credentials
3. **Logout:** Click logout in navigation

**Expected Results:**
- ✅ Signup form validates inputs
- ✅ Password stored securely (hashed)
- ✅ Login authenticates user
- ✅ Logout clears session
- ✅ Protected pages redirect to login

---

### 8. 📱 Responsive Design

**How to test:**
1. Open app in browser
2. Test on different screen sizes:
   - Desktop (1200px+)
   - Tablet (768px-1199px)
   - Mobile (< 768px)
3. Resize browser window

**Expected Results:**
- ✅ Layout adjusts smoothly
- ✅ Navigation works on all sizes
- ✅ Cards stack on mobile
- ✅ No horizontal scrolling on mobile
- ✅ Touch-friendly buttons

---

## Database Verification

### Check Saved Data

**Test Results Location:**
- Table: `dyslexia_test`
- Fields: id, user_id, test_type, analysis_results, dyslexia_probability, risk_level, recommendations, test_data, created_at

**Game Scores Location:**
- Table: `game_score`
- Fields: id, user_id, game_name, score, time_taken, difficulty, completed, created_at

**Learning Progress Location:**
- Table: `learning_progress`
- Fields: id, user_id, material_id, category, progress_percentage, completed, started_at, completed_at

---

## Test Data Summary

After complete testing, you should have:

1. **2 Dyslexia Tests:** 1 handwriting, 1 speech
2. **7 Game Scores:** One from each game
3. **9 Learning Materials:** All categories represented
4. **Dashboard Statistics:** All populated with real data

---

## Troubleshooting

### Issue: "avg_score is undefined"
**Solution:** This error is fixed. Dashboard now passes avg_score correctly.

### Issue: Game score not saving
**Solution:** 
1. Ensure you click "Save Score" button
2. Check browser console for errors (F12)
3. Restart the app

### Issue: Dyslexia test not saving
**Solution:**
1. Allow microphone/camera access
2. Complete the analysis (don't go back)
3. Check test history to confirm

### Issue: Learning materials not showing
**Solution:**
1. Refresh the page
2. Check that Flask app is running
3. Verify database connection

---

## Performance Tips

- Each test takes ~30 seconds
- Complete feature testing: ~15-20 minutes
- Test in order: Auth → Dyslexia → Games → Learning → Dashboard

---

## Success Criteria

✅ All features working as expected
✅ Data persisting in database
✅ No console errors
✅ Responsive design functioning
✅ Performance acceptable (< 2 second load time)

---

## Support

For issues:
1. Check browser console (F12 → Console tab)
2. Check Flask terminal for errors
3. Refer to README.md and DOCUMENTATION.md
4. Review error messages carefully

Happy Testing! 🚀
