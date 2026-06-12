# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The game is a number guessing game where the player tries to guess a secret number within a limited number of attempts. Hints guide the player higher or lower after each guess, and a score tracks performance.
- 7 bugs were found. The hint messages were inverted, the Hard difficulty range was narrower than Normal, wrong guesses awarded points on even attempts, the New Game button always generated a secret in the 1-100 range regardless of difficulty, the attempt counter reset to the wrong value on new games, the guess prompt hardcoded "1 and 100" for all difficulties, and a string cast on every even attempt caused lexicographic instead of numeric comparison.
- Each bug was fixed in its own commit. Logic fixes went into `logic_utils.py` and UI/state fixes went into `app.py`. A pytest case was added for each fix.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Select a difficulty from the sidebar. Easy gives a range of 1-20, Normal 1-100, and Hard 1-200.
2. Open the "Developer Debug Info" expander to see the secret number and your current attempt count.
3. Type a guess and click "Submit Guess". The hint will correctly say to go higher or lower.
4. Keep guessing. Score drops by 5 on each wrong guess and the remaining attempt count updates.
5. Guess correctly and the app shows your final score. Click "New Game" to reset and the new secret will stay within the selected difficulty range.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
======================================================================= test session starts =======================================================================
platform linux -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: /home/dizzyfrogs/Projects/AI110/ai110-module1show-gameglitchinvestigator-starter
configfile: pytest.ini
plugins: anyio-4.13.0
collected 11 items                                                                                                                                                

tests/test_game_logic.py ...........                                                                                                                        [100%]

======================================================================= 11 passed in 0.01s ========================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
