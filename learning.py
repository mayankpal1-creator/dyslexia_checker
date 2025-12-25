from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import LearningProgress, LearningMaterial

learning_bp = Blueprint('learning', __name__, url_prefix='/learning')

# Sample learning materials
LEARNING_MATERIALS = [
    {
        'id': 1,
        'title': 'Phonics Fundamentals',
        'category': 'Phonics',
        'difficulty': 'beginner',
        'description': 'Learn the basics of phonics and letter sounds',
        'content': '''
## Phonics Fundamentals

Phonics is the method of teaching reading and writing by emphasizing sound-symbol relationships. It helps readers understand that letters and letter combinations represent specific sounds.

### What is Phonics?
Phonics is a systematic approach to reading that teaches the relationship between letters (graphemes) and sounds (phonemes). This foundation is crucial for developing reading skills and is especially beneficial for individuals with dyslexia.

### Why Phonics Matters
- **Sound Recognition**: Helps identify individual letter sounds
- **Word Building**: Teaches how to blend sounds into words
- **Reading Fluency**: Improves speed and accuracy in reading
- **Spelling Skills**: Strengthens writing and spelling abilities

### The English Alphabet Sounds
- A (ay, ah, aw): **apple**, **ant**, **ball**
- B (bee): **bat**, **boy**, **bed**
- C (see, kuh): **cat**, **cup**, **city**
- D (dee): **dog**, **day**, **did**
- E (eh, ee): **egg**, **end**, **me**
- F (eff): **fun**, **fish**, **four**
- G (guh, juh): **go**, **good**, **gym**
- H (aych): **hat**, **happy**, **house**
- I (ih, eye): **it**, **in**, **ice**
- J (jay): **jump**, **job**, **jar**
- K (kay): **key**, **kit**, **king**
- L (ell): **let**, **look**, **love**
- M (em): **make**, **me**, **moon**
- N (en): **no**, **not**, **new**
- O (oh, uh): **on**, **open**, **over**
- P (pee): **play**, **put**, **pig**
- Q (kyoo): **quiet**, **queen**, **quest**
- R (are): **run**, **read**, **red**
- S (ess): **say**, **see**, **sun**
- T (tee): **to**, **take**, **top**
- U (uh, oo): **up**, **under**, **use**
- V (vee): **van**, **very**, **voice**
- W (double-you): **was**, **we**, **with**
- X (ecks): **box**, **fox**, **six**
- Y (why): **yes**, **you**, **year**
- Z (zee): **zoo**, **zero**, **zip**

### Blending Sounds
Blending is combining individual sounds into words. Practice these examples:
- c-a-t = **cat**
- d-o-g = **dog**
- b-i-g = **big**
- f-u-n = **fun**
- s-u-n = **sun**

### Practice Tips
1. Start with simple three-letter words (CVC - consonant-vowel-consonant)
2. Say each sound clearly and hold it
3. Blend the sounds together smoothly
4. Practice daily for 10-15 minutes
5. Use repetition to strengthen sound recognition

### Next Steps
After mastering basic letter sounds, progress to:
- Digraphs (two letters making one sound): **ch**, **sh**, **th**, **ph**
- Blends (consonants together): **st**, **bl**, **gr**, **tr**
- Vowel teams: **oa**, **ee**, **ai**, **ou**
        '''
    },
    {
        'id': 2,
        'title': 'Letter Sound Recognition',
        'category': 'Phonics',
        'difficulty': 'beginner',
        'description': 'Master individual letter sounds with interactive exercises',
        'content': '''
## Letter Sound Recognition

### Understanding Letter Sounds
Each letter in the English alphabet represents one or more sounds. This lesson focuses on recognizing and producing these sounds accurately.

### Short Vowel Sounds
- **A** (short): **cat**, **map**, **sad**, **bag**, **tan**
- **E** (short): **bed**, **pen**, **red**, **web**, **set**
- **I** (short): **hit**, **sit**, **bit**, **pig**, **lip**
- **O** (short): **hot**, **dog**, **top**, **box**, **got**
- **U** (short): **run**, **but**, **cut**, **mud**, **sun**

### Long Vowel Sounds
- **A** (long): **make**, **cake**, **fate**, **name**, **plate**
- **E** (long): **see**, **tree**, **bee**, **need**, **feed**
- **I** (long): **like**, **bike**, **kite**, **time**, **five**
- **O** (long): **go**, **road**, **boat**, **coat**, **tone**
- **U** (long): **use**, **fuse**, **cute**, **mute**, **tune**

### Consonant Sounds

**Hard Consonants:**
- **B**: **bat**, **ball**, **box**
- **C**: **cat**, **car**, **can** (hard C sound)
- **D**: **day**, **dog**, **did**
- **F**: **fan**, **fun**, **fox**
- **G**: **go**, **got**, **game** (hard G sound)
- **H**: **hat**, **hand**, **happy**
- **J**: **jump**, **jar**, **job**
- **K**: **key**, **king**, **keep**
- **L**: **let**, **look**, **love**
- **M**: **man**, **map**, **make**
- **N**: **no**, **not**, **new**
- **P**: **pet**, **pig**, **play**
- **R**: **red**, **run**, **rain**
- **S**: **sat**, **sun**, **sit** (soft S sound)
- **T**: **top**, **toy**, **take**
- **V**: **van**, **very**, **vest**
- **W**: **was**, **want**, **will**
- **X**: **box**, **fox**, **mix** (ends words)
- **Y**: **yes**, **you**, **yellow**
- **Z**: **zoo**, **zero**, **zip**

### Consonant Digraphs (Two letters = One sound)
- **ch**: **chip**, **chair**, **choose**
- **sh**: **ship**, **shoe**, **shop**
- **th**: **that**, **this**, **think**
- **ph**: **phone**, **photo**, **phrase**
- **wh**: **what**, **when**, **which**

### Soft and Hard Sounds
Some letters have multiple sounds:

**C** can be soft or hard:
- Hard C (k sound): **cat**, **call**, **come**
- Soft C (s sound): **city**, **cent**, **circle**

**G** can be soft or hard:
- Hard G (guh sound): **go**, **get**, **good**
- Soft G (j sound): **gym**, **giant**, **giraffe**

**S** can be soft or hard:
- Soft S (z sound): **rose**, **easy**, **used**
- Hard S (s sound): **sat**, **sun**, **sister**

### Interactive Practice
1. **Sound Discrimination**: Identify which word has the target sound
2. **Rhyming Words**: Find words that rhyme using the same sounds
3. **Word Sorting**: Group words by their beginning or ending sounds
4. **Sound Repetition**: Say words aloud repeatedly to strengthen muscle memory

### Tips for Success
- Pronounce each sound clearly
- Exaggerate mouth movements
- Practice in front of a mirror
- Record yourself and listen back
- Use multi-sensory learning (see, say, hear, write)
        '''
    },
    {
        'id': 3,
        'title': 'Sight Words Training',
        'category': 'Sight Words',
        'difficulty': 'beginner',
        'description': 'Learn and master common words that appear frequently in texts',
        'content': '''
## Sight Words Training

### What Are Sight Words?
Sight words are common words that should be recognized instantly without sounding them out. These words are crucial for reading fluency and often don't follow phonetic patterns.

### Why Learn Sight Words?
- **Reading Speed**: Recognizing sight words increases reading speed
- **Fluency**: Reduces the need to decode every word
- **Frequency**: These words appear in almost every text
- **Foundation**: Essential building blocks for reading comprehension

### The Top 100 Sight Words

**Group 1: Common Function Words**
- **a**, **an**, **the** (articles)
- **and**, **but**, **or** (conjunctions)
- **is**, **are**, **was**, **were**, **be**, **been**, **being** (to be verbs)
- **have**, **has**, **had** (to have verbs)
- **do**, **does**, **did** (to do verbs)
- **go**, **goes**, **going**, **gone** (movement)
- **can**, **could**, **may**, **might** (modals)
- **will**, **would**, **should** (future/conditional)
- **in**, **on**, **at**, **to**, **from** (prepositions)

**Group 2: Personal Pronouns**
- **I**, **me**, **my**, **we**, **us**, **our**
- **you**, **your**, **he**, **him**, **his**
- **she**, **her**, **it**, **its**, **they**, **them**, **their**

**Group 3: Common Nouns and Verbs**
- **people**, **person**, **man**, **woman**, **child**, **boy**, **girl**
- **say**, **said**, **say**, **tell**, **told**
- **make**, **made**, **get**, **got**, **put**, **come**, **came**
- **see**, **saw**, **know**, **knew**, **think**, **thought**
- **want**, **like**, **love**, **need**, **use**

**Group 4: Common Adjectives and Adverbs**
- **good**, **bad**, **big**, **small**, **new**, **old**
- **first**, **last**, **other**, **same**, **different**
- **very**, **much**, **more**, **most**, **some**, **all**
- **here**, **there**, **where**, **now**, **then**

**Group 5: High-Frequency Words**
- **the**, **be**, **to**, **of**, **and**, **a**, **in**, **that**, **have**
- **it**, **for**, **not**, **on**, **with**, **he**, **as**, **you**, **do**
- **at**, **this**, **but**, **his**, **by**, **from**, **they**, **we**, **say**

### Sight Word Learning Strategies

**Visual Learning**
- Write words on flashcards
- Create word walls in the room
- Use different colors for different words
- Draw pictures associated with words

**Auditory Learning**
- Say words aloud repeatedly
- Listen to words being pronounced
- Create rhymes or songs with sight words
- Spell words out loud

**Kinesthetic Learning**
- Write words in sand or shaving cream
- Trace letters with fingers
- Type words repeatedly
- Act out words that describe actions

**Contextual Learning**
- Read words in sentences
- Create word families
- Use words in conversations
- Read books featuring sight words

### Practice Activities

1. **Flashcard Drills**: Review 5-10 words daily
2. **Sentence Building**: Create sentences using sight words
3. **Word Search**: Find sight words in a grid
4. **Missing Letter**: Fill in missing letters in sight words
5. **Matching**: Match words to pictures or definitions
6. **Speed Reading**: Time how fast you can read sight word lists

### Recommended Learning Path
- Week 1-2: Master 10 words
- Week 3-4: Add 10 more words (total 20)
- Week 5-6: Add 10 more words (total 30)
- Continue adding 10 words every 2 weeks until mastery

### Tips for Success
- Practice daily for 10-15 minutes
- Mix old and new words in practice sessions
- Use multiple learning modalities
- Celebrate progress and mastery
- Create a personal sight word dictionary
- Apply sight words while reading books
        '''
    },
    {
        'id': 4,
        'title': 'Reading Comprehension Exercises',
        'category': 'Reading',
        'difficulty': 'intermediate',
        'description': 'Develop skills to understand and analyze what you read',
        'content': '''
## Reading Comprehension Exercises

### What is Reading Comprehension?
Reading comprehension is the ability to process text, understand its meaning, retain information, and apply it to new situations. It's not just about reading words—it's about understanding ideas.

### The 5 Key Components of Comprehension

**1. Vocabulary**
Understanding the meaning of words is fundamental to comprehension.
- Learn new words in context
- Use context clues to determine meaning
- Build a personal vocabulary journal
- Understand multiple meanings of words

**2. Fluency**
Reading smoothly and at an appropriate pace helps comprehension.
- Don't rush or read too slowly
- Use proper intonation and expression
- Pause at punctuation marks
- Focus on understanding, not speed

**3. Prior Knowledge**
Your existing knowledge helps you understand new information.
- Connect new ideas to what you already know
- Ask: "How does this relate to something I know?"
- Build background knowledge on topics
- Activate prior knowledge before reading

**4. Working Memory**
The ability to hold information in mind while reading.
- Take notes while reading
- Summarize paragraphs as you go
- Reread difficult sections
- Use mental imagery to visualize content

**5. Inference and Analysis**
Drawing conclusions and making connections.
- Read between the lines
- Make predictions about what might happen
- Identify the author's purpose
- Distinguish between facts and opinions

### Comprehension Strategies

**Before Reading: Preparation**
- Look at the title and predict what it's about
- Preview headings and illustrations
- Activate prior knowledge
- Set a purpose for reading
- Skim to get an overview

**During Reading: Active Engagement**
- Ask questions as you read
- Make predictions
- Connect to personal experiences
- Visualize descriptions
- Notice confusing parts and reread
- Identify main ideas and supporting details

**After Reading: Reflection**
- Summarize what you read
- Answer comprehension questions
- Discuss with others
- Review difficult concepts
- Apply what you learned

### Question Types to Practice

**Literal Comprehension** (facts directly stated)
- What is the character's name?
- When did the story take place?
- Where does the character live?

**Inferential Comprehension** (reading between the lines)
- Why did the character do this?
- What will happen next?
- How does the character feel?

**Evaluative Comprehension** (making judgments)
- Do you agree with the character's actions?
- Is this a good solution? Why or why not?
- Would you do the same thing?

### Practice Passage

**The Little Library**

Marcus discovered an old wooden box in his grandmother's attic. Inside were dozens of books with worn covers and yellowed pages. His grandmother smiled as he carefully lifted each one. "These were my favorite books when I was your age," she said. Marcus opened one with a beautiful illustrated cover. As he read the first page, he felt transported to a magical kingdom. Hours passed as he lost himself in the stories. From that day on, Marcus visited his grandmother's attic regularly, and they shared stories together.

**Comprehension Questions:**
1. Where did Marcus find the books? (Literal)
2. Why did Marcus's grandmother show him these books? (Inferential)
3. Do you think Marcus enjoyed reading? Explain. (Evaluative)
4. What do you predict Marcus will do next time he visits? (Inferential)

### Tips for Success
- Read in a quiet environment
- Don't rush through text
- Reread confusing passages
- Keep a reading journal
- Discuss books with others
- Ask questions when confused
- Practice active reading strategies
- Read regularly to improve skills
        '''
    },
    {
        'id': 5,
        'title': 'Vocabulary Building',
        'category': 'Vocabulary',
        'difficulty': 'intermediate',
        'description': 'Expand your vocabulary and improve word knowledge',
        'content': '''
## Vocabulary Building

### Why Build Vocabulary?
A strong vocabulary is essential for:
- **Reading Comprehension**: Understand more texts accurately
- **Communication**: Express yourself more precisely
- **Academic Success**: Perform better in school
- **Professional Growth**: Excel in careers
- **Confidence**: Speak and write with greater assurance

### Methods to Learn New Words

**1. Context Clues**
Many times you can determine a word's meaning from surrounding text.
- **Definition Clues**: The author explains the word directly
  Example: "The tsunami, a giant ocean wave, destroyed the village."
- **Example Clues**: Examples help clarify meaning
  Example: "Utensils like forks, spoons, and knives are dining tools."
- **Contrast Clues**: Opposite words reveal meaning
  Example: "She was loquacious, unlike her silent sister."
- **Logic/Experience Clues**: Your knowledge helps you infer
  Example: "The nocturnal animal hunts at night."

**2. Word Parts (Morphology)**
Understanding roots, prefixes, and suffixes helps decode unknown words.

**Common Prefixes:**
- **un-**: not (unhappy, undo, unable)
- **re-**: again (redo, replay, rewrite)
- **pre-**: before (preview, predict, preschool)
- **dis-**: not, opposite (disagree, disappear, dislike)
- **mis-**: wrong (mistake, misunderstand, misplace)
- **over-**: too much (overflow, overtake, oversleep)
- **under-**: beneath, not enough (understand, underground, underage)
- **sub-**: under (submarine, subway, submerge)

**Common Suffixes:**
- **-tion/-sion**: action or condition (action, education, tension)
- **-ment**: state or condition (enjoyment, government, agreement)
- **-ness**: quality or state (happiness, darkness, kindness)
- **-able/-ible**: capable of (readable, comfortable, possible)
- **-ful**: full of (joyful, powerful, helpful)
- **-less**: without (hopeless, careless, homeless)
- **-er/-or**: one who (teacher, actor, runner)
- **-ly**: in the manner of (quickly, carefully, loudly)
- **-ing**: present participle (running, reading, singing)
- **-ed**: past tense (walked, talked, opened)

**Common Roots:**
- **dict**: speak (dictate, dictionary, predict)
- **port**: carry (portable, transport, airport)
- **scrib/script**: write (describe, prescription, transcript)
- **mit/miss**: send (permit, missile, submit)
- **graph**: write (paragraph, biography, photograph)
- **phon**: sound (telephone, microphone, symphony)
- **struct**: build (structure, construct, instruct)

**3. Flashcards and Spaced Repetition**
- Create cards with word on one side, definition on the other
- Review regularly in intervals
- Mix reviewed and new cards
- Use apps like Quizlet for digital flashcards

**4. Word Journals**
- Keep a notebook of new words
- Write the word, definition, pronunciation, and example sentence
- Review periodically
- Use words in conversation

**5. Reading and Listening**
- Read books, articles, and blogs
- Listen to podcasts and audiobooks
- Watch educational videos
- Pay attention to new words in context

### Word Categories to Learn

**Action Words (Verbs):**
- Basic: walk, run, eat, sleep
- Advanced: amble, sprint, consume, slumber

**Describing Words (Adjectives):**
- Basic: big, small, happy, sad
- Advanced: enormous, diminutive, elated, melancholy

**Emotion Words:**
- Happy variations: joyful, delighted, ecstatic, cheerful
- Sad variations: gloomy, dejected, sorrowful, melancholic
- Angry variations: furious, irate, enraged, livid

**Synonyms and Antonyms**
- **Synonyms** are words with similar meanings
  - Beautiful: lovely, pretty, gorgeous, stunning
  - Fast: quick, rapid, swift, speedy
  
- **Antonyms** are words with opposite meanings
  - Hot ↔ Cold
  - Happy ↔ Sad
  - Beginning ↔ End

### Vocabulary Building Plan
- **Daily**: Learn 1-2 new words
- **Weekly**: Review all new words from the week
- **Monthly**: Consolidate learning and practice usage
- **Quarterly**: Assess vocabulary growth

### Tips for Success
- Learn words in context, not just definitions
- Use new words in speaking and writing
- Create mental images for abstract words
- Group related words together
- Practice with synonyms and antonyms
- Read challenging materials regularly
- Engage in discussions using new vocabulary
- Keep consistent with your learning routine
        '''
    },
    {
        'id': 6,
        'title': 'Spelling Practice',
        'category': 'Spelling',
        'difficulty': 'intermediate',
        'description': 'Master correct spelling and improve writing accuracy',
        'content': '''
## Spelling Practice

### Why Spelling Matters
- **Clear Communication**: Correct spelling ensures your message is understood
- **Professional Appearance**: Good spelling reflects well on your work
- **Reading Connection**: Spelling and reading are interconnected
- **Confidence**: Correct spelling boosts writing confidence
- **Academic Success**: Spelling accuracy impacts grades

### Common Spelling Rules

**1. I Before E (Usually)**
Rule: **i** comes before **e** except after **c** or when sounding like "ay"
- **i** before **e**: believe, piece, field, chief, brief
- Except after **c**: receive, deceive, ceiling, conceit
- Except "ay" sound: eight, vein, rein, weigh, neigh

**Exceptions**: weird, their, seize, height, neither

**2. Silent E Rule**
A silent **e** at the end often makes the vowel "long"
- make (mā-k), not mak
- kite (kī-t), not kit
- cute (kū-t), not cut
- mane (mā-n), not man

When adding suffixes:
- **Drop e** before a vowel: make → making, write → writing
- **Keep e** before a consonant: make → makeable, safe → safely

**3. Doubling the Final Consonant**
When a one-syllable word ends in consonant-vowel-consonant (CVC), double the final consonant before adding a suffix beginning with a vowel.
- stop → stopped, stopping
- run → running
- sit → sitting
- plan → planning

**Conditions:**
- One syllable (or stress on last syllable for multisyllabic words)
- Ends in CVC pattern
- Adding a suffix starting with a vowel

**4. Y to I Rule**
When **y** is at the end of a word and you're adding a suffix, change **y** to **i** (unless the suffix starts with **i**)
- happy → happier, happiness
- easy → easier, easily
- silly → sillier, silliness
- baby → babies (but: babying)

**5. Vowel Team Rule**
When two vowels go walking, the first one does the talking (usually)
- **ai**: rain, pain, main, train
- **ea**: read, meat, bread (exceptions exist)
- **oa**: boat, road, coat, toad
- **ue**: blue, glue, true, due

**6. Q Without U**
Words with **q** almost always have **u** after it
- quiet, queen, question, quick, quality, acquaint
- **Exceptions**: qi (Chinese philosophical concept)

**7. Prefixes and Suffixes**
- Spelling doesn't change when adding prefixes: un- + do = undo, mis- + spell = misspell
- Spelling often changes when adding suffixes (see rules above)

### Commonly Misspelled Words

**High-Frequency Mistakes:**
- **receive/recieve**: receive (i before e)
- **their/there/they're**: their (possessive), there (location), they're (they are)
- **your/you're**: your (possessive), you're (you are)
- **its/it's**: its (possessive), it's (it is)
- **separate**: sep-a-rate (not seperate)
- **accommodate**: accommodate (double c, double m)
- **necessary**: one collar, two sleeves (n-e-c-e-s-s-a-r-y)
- **privilege**: i-l-e-g-e (not priveledge)
- **embarrass**: red face (remember r's and s's)
- **rhythm**: r-h-y-t-h-m (has no vowels except y)
- **beginning**: double n (begin → beginning)
- **occassion/occasion**: occasion (one c, double s)
- **weird**: i before e? Except this weird one!
- **conscience/conscious**: conscience (science of right and wrong), conscious (aware)

### Spelling by Patterns

**Words Ending in -tion:**
- action, nation, motion, ocean, lotion

**Words Ending in -sion:**
- tension, pension, mansion, occasion, compression

**Words Ending in -able:**
- comfortable, capable, readable, remarkable, reliable

**Words Ending in -ible:**
- possible, terrible, horrible, visible, compatible

**Words Ending in -ful:**
- beautiful, wonderful, careful, helpful, grateful

**Words Ending in -ness:**
- happiness, kindness, darkness, wellness, awareness

### Spelling Practice Strategies

**1. Multi-Sensory Learning**
- **See**: Read the word and visualize it
- **Say**: Pronounce the word aloud
- **Hear**: Listen to the word spelled out
- **Write**: Write the word by hand
- **Use**: Write the word in a sentence

**2. Mnemonics**
Create memory devices:
- **NECESSARY**: Never Eat Cereal, Eat Salad, Apples, Rice, You
- **RHYTHM**: Rhythm Helps Your Two Hips Move
- **BECAUSE**: Big Elephants Can Always Understand Small Elephants

**3. Word Families**
Group related words:
- Words ending in -light: moonlight, daylight, sunlight, flashlight
- Words with silent letters: know, knife, psychology, pterodactyl

**4. Spelling Journal**
- Write down words you misspell
- Review them regularly
- Track your progress

**5. Dictionary Practice**
- Look up correct spellings
- Note pronunciation guides
- Study word origins
- Learn related words

### Practice Tips
- **Daily Practice**: 10-15 minutes daily is better than longer sessions
- **Use Dictionaries**: When in doubt, look it up
- **Proofread Carefully**: Read your writing multiple times
- **Use Technology**: Spell-check, but don't rely on it solely
- **Read Actively**: Notice how words are spelled in what you read
- **Practice Frequently Misspelled Words**: Focus on your personal weak areas
- **Write Often**: The more you write, the better your spelling becomes
- **Be Patient**: Spelling improvement takes time and consistent practice
        '''
    },
    {
        'id': 7,
        'title': 'Reading Fluency',
        'category': 'Reading',
        'difficulty': 'intermediate',
        'description': 'Read smoothly, accurately, and with proper expression',
        'content': '''
## Reading Fluency

### What is Reading Fluency?
Reading fluency is the ability to read text quickly, accurately, and with expression. It involves:
- **Accuracy**: Reading words correctly
- **Speed**: Reading at an appropriate pace
- **Expression**: Using proper intonation and phrasing
- **Automaticity**: Recognizing words automatically without conscious effort

### Why Fluency Matters
- **Comprehension**: Fluent readers understand better
- **Engagement**: Fluency makes reading enjoyable
- **Confidence**: Fluent readers feel more confident
- **Efficiency**: Reading faster frees mental resources for understanding
- **Professionalism**: Clear, fluent reading impresses others

### The Four Components of Fluency

**1. Accuracy**
Reading words correctly on the first try.
- Practice sight words until automatic
- Use context clues for unfamiliar words
- Slow down and reread difficult passages
- Ask for help with challenging words

**2. Rate/Speed**
Reading at an appropriate pace.
- Good pace: 150-200 words per minute for adults
- Too fast: You miss comprehension
- Too slow: Loses meaning and engagement
- Varied pace: Speed up for simple text, slow down for complex ideas

**3. Expression/Prosody**
Reading with appropriate intonation, stress, and phrasing.
- **Intonation**: Vary pitch and tone
- **Stress**: Emphasize important words
- **Phrasing**: Group words meaningfully
- **Punctuation**: Pause at commas, stop at periods

**4. Automaticity**
Recognizing words without conscious effort.
- High-frequency words should be automatic
- Reduces cognitive load
- Allows focus on comprehension
- Develops with practice

### Techniques to Improve Fluency

**1. Repeated Reading**
Read the same passage multiple times to build automaticity and expression.
- First read: Focus on accuracy
- Second read: Increase speed while maintaining accuracy
- Third read: Add expression and natural rhythm
- Benefits: 10-15% improvement in speed and comprehension

**2. Choral Reading**
Read aloud together with others.
- Listen to the rhythm and flow
- Hear proper pronunciation
- Match the pace of skilled readers
- Reduces anxiety about reading aloud

**3. Echo Reading**
Adult or fluent reader reads first, student repeats.
- Models correct pronunciation and expression
- Gives time to process before producing
- Builds confidence
- Great for struggling readers

**4. Audio-Assisted Reading**
Listen to audiobook while reading along in the text.
- Hears proper expression and pacing
- Visual input reinforces auditory input
- Combines multiple modalities
- Increases engagement

**5. Reader's Theater**
Dramatic reading of scripts with multiple readers.
- Motivates expressive reading
- Provides practice opportunity
- Builds fluency in engaging context
- Increases confidence

### Phrasing Practice

Rather than reading word by word, group words into meaningful phrases.

**Wrong (Word-by-Word):**
"The / quick / brown / fox / jumps / over / the / lazy / dog"

**Right (Meaningful Phrases):**
"The quick brown fox / jumps over / the lazy dog"

**Example Practice:**
*Original:* "She walked to the store, but she forgot her money at home."
*Phrased:* "She walked to the store, / but she forgot her money at home."

### Expression Guidelines

**Question Marks (?):**
Raise your pitch at the end of questions.
"Are you ready to go?"

**Exclamation Marks (!):**
Show excitement or emphasis.
"What an amazing discovery!"

**Commas (,):**
Slight pause and continue thought.
"After breakfast, we went to school."

**Periods (.):**
Complete stop and pause.
"The game was over."

**Dialogue:**
Vary voice based on character emotions.
- Angry character: Harsh, loud tone
- Sad character: Soft, slow tone
- Happy character: Bright, fast tone

### Fluency Building Plan

**Week 1-2: Accuracy Focus**
- Read slowly and carefully
- Focus on pronouncing each word correctly
- Use context clues for difficult words
- Reread any misread words

**Week 3-4: Speed Development**
- Gradually increase reading pace
- Maintain accuracy
- Time your reading and track speed
- Aim for smooth, continuous reading

**Week 5-6: Expression**
- Add intonation and stress
- Vary pace based on meaning
- Pause at appropriate places
- Let emotion guide your voice

**Week 7-8: Integration**
- Combine accuracy, speed, and expression
- Read for comprehension
- Enjoy the reading experience
- Assess progress

### Assessment Measures

**Words Per Minute (WPM)**
- Beginner: 50-100 WPM
- Intermediate: 100-150 WPM
- Advanced: 150-200+ WPM

**Accuracy Rate**
- Count errors out of 100 words read
- Target: 95% accuracy or better
- Example: 2 errors in 100 words = 98% accuracy

**Comprehension Score**
- Answer comprehension questions correctly
- Demonstrate understanding of main ideas
- Target: 70-80% comprehension

### Tips for Success
- Practice daily, even 10-15 minutes helps
- Choose interesting materials to read
- Read aloud to family or friends
- Don't rush—quality over speed
- Focus on understanding, not just speed
- Use expression to make reading engaging
- Celebrate progress and improvements
- Be patient—fluency develops over time
        '''
    },
    {
        'id': 8,
        'title': 'Advanced Reading Materials',
        'category': 'Reading',
        'difficulty': 'advanced',
        'description': 'Explore complex texts, literature, and challenging reading materials',
        'content': '''
## Advanced Reading Materials

### What Makes Reading Advanced?
Advanced reading involves:
- **Complex Vocabulary**: Sophisticated and specialized terms
- **Complex Sentence Structures**: Multi-clause sentences and varied syntax
- **Thematic Depth**: Explore complex ideas and abstract concepts
- **Literary Techniques**: Symbolism, metaphor, irony, foreshadowing
- **Critical Analysis**: Evaluate arguments and interpret meaning

### Types of Advanced Texts

**1. Literature and Fiction**
Classic and contemporary novels with depth and complexity.
- Character development across hundreds of pages
- Interconnected plots and subplots
- Deeper exploration of human nature and society
- Literary devices enhancing meaning

**Examples:**
- Pride and Prejudice by Jane Austen
- 1984 by George Orwell
- To Kill a Mockingbird by Harper Lee
- The Great Gatsby by F. Scott Fitzgerald
- Jane Eyre by Charlotte Brontë

**2. Non-Fiction and Essays**
Serious exploration of real-world topics and ideas.
- Historical events and biographies
- Scientific explanations and discoveries
- Philosophy and ethics
- Cultural and social commentary

**Examples:**
- The Immortal Life of Henrietta Lacks by Rebecca Skloot
- Educated by Tara Westover
- Thinking, Fast and Slow by Daniel Kahneman
- A Brief History of Time by Stephen Hawking

**3. Poetry**
Concentrated language with multiple layers of meaning.
- Rhythm and rhyme patterns
- Imagery and symbolism
- Emotional resonance
- Cultural significance

**Examples:**
- Shakespeare's Sonnets
- "The Road Not Taken" by Robert Frost
- Harlem Renaissance poetry by Langston Hughes
- Contemporary poetry by Maya Angelou

**4. Academic and Scholarly Texts**
Dense, technical writing about specific fields.
- Research papers and case studies
- Journal articles
- Technical documentation
- Theoretical works

**5. News and Opinion**
Nuanced discussion of current events and complex issues.
- News analysis and long-form journalism
- Opinion essays and editorials
- Investigative reporting
- Political commentary

### Literary Devices and Techniques

**Metaphor**
Direct comparison between two unlike things without using "like" or "as"
- "Time is money"
- "Life is a journey"
- "The world is a stage"

**Simile**
Comparison using "like" or "as"
- "She was as quiet as a mouse"
- "His heart was like stone"
- "The night fell like a curtain"

**Symbolism**
Objects, characters, or actions representing larger ideas.
- A white dove symbolizes peace
- Darkness represents evil or ignorance
- A mirror represents self-reflection

**Irony**
Contradiction between expected and actual meaning.
- **Verbal irony**: Saying one thing but meaning another
- **Situational irony**: The opposite of what is expected happens
- **Dramatic irony**: Reader knows something characters don't

**Foreshadowing**
Hints about future events in the story.
- Creates suspense and interest
- Helps readers make predictions
- Provides clues to uncover on rereading

**Tone and Mood**
- **Tone**: Author's attitude toward subject
- **Mood**: Feeling or atmosphere created for reader

**Imagery**
Vivid descriptive language appealing to senses.
- Visual: colors, shapes, light
- Auditory: sounds and speech
- Olfactory: smells
- Tactile: textures and sensations
- Gustatory: tastes

### Reading Strategies for Advanced Texts

**Pre-Reading Strategies**
1. Read the title and think about what it suggests
2. Read the author's biography and publication date
3. Skim headings, summaries, and introductions
4. Note any questions you want answered
5. Activate prior knowledge about the topic
6. Set a purpose for reading

**During-Reading Strategies**
1. Annotate: Write comments and questions in margins
2. Highlight: Mark key passages and important ideas
3. Question: Ask yourself about meaning and purpose
4. Predict: Make guesses about what comes next
5. Connect: Link new information to what you know
6. Visualize: Create mental images of descriptions
7. Clarify: Stop and reread confusing parts

**After-Reading Strategies**
1. Summarize: Write a brief overview of main ideas
2. Analyze: Examine techniques and meaning
3. Discuss: Share thoughts with others
4. Evaluate: Judge the work's quality and impact
5. Reflect: Consider how ideas relate to your life
6. Research: Learn more about related topics

### Critical Reading Skills

**Distinguishing Fact from Opinion**
- **Facts**: Statements that can be verified
- **Opinions**: Beliefs, judgments, or interpretations

**Identifying Author's Purpose**
- To inform: Provide information
- To persuade: Convince reader of a viewpoint
- To entertain: Provide enjoyment
- To inspire: Move reader emotionally

**Evaluating Arguments**
- Are claims supported with evidence?
- Is the evidence credible and relevant?
- Are there logical fallacies?
- Are counterarguments acknowledged?

**Recognizing Bias**
- Author's personal beliefs influencing presentation
- One-sided presentation of information
- Loaded language designed to provoke emotion
- Omission of important information

### Building Reading Lists

**Classic Literature**
- Austen, Brontë, Dickens, Austen, Twain
- Russian literature: Tolstoy, Dostoevsky
- Modern classics: Morrison, McCarthy, Lahiri

**Contemporary Fiction**
- Award winners (Pulitzer, Man Booker)
- Bestselling authors
- Emerging voices in literature
- Genre classics (Mystery, Sci-Fi, Fantasy)

**Non-Fiction**
- Biography and memoir
- History and politics
- Science and nature
- Philosophy and self-help

**Poetry Collections**
- Established poets
- Contemporary voices
- Poetry from different cultures
- Themed collections

### Tips for Success
- Don't rush—allow time for reflection
- Keep a reader's journal
- Join a book club for discussion
- Reread challenging passages multiple times
- Look up unfamiliar words and references
- Consider multiple interpretations
- Read critically but enjoyably
- Challenge yourself with new genres and authors
- Let reading expand your perspectives
        '''
    },
    {
        'id': 9,
        'title': 'Creative Writing',
        'category': 'Writing',
        'difficulty': 'advanced',
        'description': 'Develop your creative expression through writing and storytelling',
        'content': '''
## Creative Writing

### What is Creative Writing?
Creative writing is writing that expresses ideas, emotions, and imagination rather than simply reporting facts. It includes:
- **Fiction**: Stories created from imagination
- **Poetry**: Concentrated, artistic expression
- **Personal Narrative**: True stories told artistically
- **Memoirs**: Personal life experiences
- **Scriptwriting**: Dialogue-driven formats for film, theater, and television

### Why Write Creatively?
- **Self-Expression**: Share your unique voice and perspective
- **Emotional Processing**: Work through feelings and experiences
- **Imagination Development**: Enhance creative thinking
- **Communication Skills**: Learn to convey ideas effectively
- **Personal Fulfillment**: Experience joy of creating

### Elements of Fiction Writing

**Plot**
The sequence of events that make up a story.
- **Exposition**: Introduction to characters and setting
- **Rising Action**: Events building toward climax
- **Climax**: Most intense moment; turning point
- **Falling Action**: Events after climax leading to resolution
- **Resolution**: How the story ends and conflicts are resolved

**Character Development**
Creating believable, complex characters.
- **Physical Description**: Appearance and mannerisms
- **Personality**: Traits, quirks, and tendencies
- **Motivation**: What drives the character's actions
- **Conflict**: Internal or external struggles
- **Growth**: How characters change through the story
- **Dialogue**: How characters speak reveals personality

**Setting**
The time and place where the story occurs.
- **Time**: Historical period, time of day, time span
- **Place**: Geographic location and specific details
- **Culture**: Social and cultural context
- **Atmosphere**: Mood created by setting
- **Sensory Details**: Sights, sounds, smells, tastes, textures

**Conflict**
The central problem or struggle in the story.
- **Person vs. Person**: Character against another character
- **Person vs. Self**: Internal struggle and personal growth
- **Person vs. Society**: Character fighting social norms or injustice
- **Person vs. Nature**: Character against natural forces
- **Person vs. Technology**: Character against artificial systems

**Theme**
The underlying idea or message of the story.
- The author's commentary on human nature, society, love, etc.
- Not explicitly stated but woven throughout
- Revealed through character actions and plot events
- Readers discover meaning through interpretation

### Point of View

**First Person (I/We)**
- Story told by a character in the story
- Reader sees only what this character sees
- Creates intimacy but limited perspective
- Example: "I walked into the room and immediately knew something was wrong."

**Second Person (You)**
- Rare perspective; addresses reader directly
- Creates immediate involvement
- Can feel experimental or preachy
- Example: "You open the door and gasp at what you see."

**Third Person Limited**
- Story told by narrator about character, using "he/she/they"
- Limited to one character's thoughts and knowledge
- Balances objectivity with intimacy
- Example: "She wondered what he was hiding."

**Third Person Omniscient**
- Narrator knows all characters' thoughts and feelings
- Can move between characters' perspectives
- Provides comprehensive view but less intimacy
- Example: "She wanted to leave, but he hoped she'd stay."

### Writing Techniques

**Show, Don't Tell**
Rather than stating emotions or facts, demonstrate them through action and description.

**Tell (Weak):**
"She was nervous about the presentation."

**Show (Strong):**
"Her hands trembled as she adjusted the microphone. She cleared her throat three times before speaking."

**Using Vivid Description**
Engage multiple senses and create specific images.

**Weak:**
"The garden was beautiful."

**Strong:**
"The garden overflowed with crimson roses and golden sunflowers. The sweet fragrance of jasmine floated on the warm breeze. Bees hummed contentedly as they moved from flower to flower."

**Dialogue**
Realistic conversation revealing character and advancing plot.

**Poor Dialogue:**
"Hello. How are you?" said John.
"I am fine," said Mary. "How are you?"

**Better Dialogue:**
"Hey, how's it going?" John asked.
"Not bad. You?" Mary shoved her hands in her pockets.

**Pacing**
Managing the speed of story revelation.
- Short sentences: Create tension and urgency
- Long sentences: Build atmosphere and reflection
- Paragraph breaks: Control reading rhythm
- Action: Speeds up pacing
- Description: Slows down pacing

### Poetry Techniques

**Rhyme**
Words with similar ending sounds.
- **End rhyme**: Words at line endings rhyme
- **Internal rhyme**: Rhyme within a line
- **Slant rhyme**: Near rhyme but not perfect
- **No rhyme**: Free verse

**Meter and Rhythm**
The pattern of stressed and unstressed syllables.
- Creates musical quality
- Can be regular or varied
- Affects how the poem is read aloud
- Creates emotional impact

**Imagery and Sensory Language**
Vivid descriptions appealing to the senses.
- Creates visual pictures in reader's mind
- Enhances emotional connection
- Engages multiple senses
- Makes abstract ideas concrete

**Figurative Language**
Non-literal language creating comparison or effect.
- Metaphor: Direct comparison without "like" or "as"
- Simile: Comparison using "like" or "as"
- Personification: Giving human qualities to non-human things
- Hyperbole: Extreme exaggeration for effect
- Alliteration: Repeated initial consonant sounds

**Line Breaks**
Deliberate ending of lines for effect.
- Creates natural pauses
- Emphasizes certain words
- Controls pacing and rhythm
- Creates visual shape on page

### Genres of Creative Writing

**Short Stories**
- Complete narratives in limited space
- Focus on single event or revelation
- Fewer characters and simpler plots than novels
- Powerful use of literary techniques

**Novels**
- Long-form narratives with complex plots
- Multiple characters with depth
- Subplots and secondary storylines
- Extended development of themes

**Memoir**
- True stories from author's life
- Personal perspective and reflection
- Explores meaning and significance
- Blends fact with personal interpretation

**Fantasy and Science Fiction**
- Imagined worlds with their own rules
- Often explore philosophical questions
- Adventure and wonder combined with meaning
- Can comment on our real world

**Mystery and Thriller**
- Plot-driven with suspense
- Secrets and revelations drive narrative
- Multiple perspectives and red herrings
- Resolution that surprises yet satisfies

**Romance**
- Central plot focuses on romantic relationship
- Explores emotional development between characters
- Happy or meaningful ending
- Various subgenres: contemporary, fantasy, historical, etc.

### The Writing Process

**Brainstorming**
- Generate ideas without judgment
- Write freely and explore possibilities
- Ask "what if" questions
- Create characters and scenarios

**Drafting**
- Write the first draft without editing
- Get ideas on paper quickly
- Don't worry about perfection
- Focus on story and creation

**Revising**
- Reread and identify areas for improvement
- Reorganize and restructure as needed
- Add or cut scenes
- Strengthen weak areas

**Editing**
- Fine-tune language and style
- Check grammar and spelling
- Improve clarity and word choice
- Ensure consistency

**Proofreading**
- Final check for errors
- Read aloud to catch mistakes
- Check formatting and presentation
- Final polish before sharing

### Tips for Success
- **Read widely**: Study how professional writers work
- **Write regularly**: Daily practice improves skills
- **Write what interests you**: Passion shows in writing
- **Don't fear failure**: First drafts are rarely perfect
- **Get feedback**: Share work with trusted readers
- **Revise thoroughly**: Great writing is rewriting
- **Find your voice**: Develop your unique style
- **Read your work aloud**: Hear how it sounds
- **Keep a journal**: Practice writing daily
- **Enjoy the process**: Writing should be rewarding
        '''
    },
]

@learning_bp.route('/')
@login_required
def index():
    materials = LEARNING_MATERIALS
    return render_template('learning_materials.html', materials=materials)

@learning_bp.route('/material/<int:material_id>')
@login_required
def material_detail(material_id):
    material = next((m for m in LEARNING_MATERIALS if m['id'] == material_id), None)
    if not material:
        return jsonify({'error': 'Material not found'}), 404
    
    # Always return JSON for this endpoint (used by AJAX client)
    return jsonify({'success': True, 'material': material})

@learning_bp.route('/start/<int:material_id>', methods=['POST'])
@login_required
def start_material(material_id):
    material = next((m for m in LEARNING_MATERIALS if m['id'] == material_id), None)
    if not material:
        return jsonify({'error': 'Material not found'}), 404
    
    # Check if already started
    progress = LearningProgress.query.filter_by(
        user_id=current_user.id,
        material_id=material_id
    ).first()
    
    if not progress:
        progress = LearningProgress(
            user_id=current_user.id,
            material_id=material_id,
            material_title=material['title'],
            category=material['category']
        )
        db.session.add(progress)
        db.session.commit()
    
    return jsonify({'success': True, 'progress_id': progress.id})

@learning_bp.route('/update-progress/<int:material_id>', methods=['POST'])
@login_required
def update_progress(material_id):
    try:
        data = request.json
        progress = LearningProgress.query.filter_by(
            user_id=current_user.id,
            material_id=material_id
        ).first()
        
        if not progress:
            return jsonify({'error': 'Progress not found'}), 404
        
        progress.progress_percentage = data.get('progress', 0)
        if data.get('completed'):
            progress.completed = True
            from datetime import datetime
            progress.completed_at = datetime.utcnow()
        
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@learning_bp.route('/progress')
@login_required
def user_progress():
    progress = LearningProgress.query.filter_by(user_id=current_user.id).all()
    return render_template('learning_progress.html', progress=progress)
