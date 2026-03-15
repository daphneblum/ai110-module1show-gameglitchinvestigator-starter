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

- [ ] Describe the game's purpose.
The purpose of the game is to use the hints of "too low" and "too high" to guess the secret number that is in a specific range based on the chosen difficulty level. This logic is often used to teach coding students recursion.

- [ ] Detail which bugs you found.

Hint messages were reversed.
Easy mode could generate a secret number outside the expected range.
The New Game button did not fully reset the game.
Score behavior was inconsistent.
The secret number was not stable across Streamlit reruns.

- [ ] Explain what fixes you applied.

Corrected the higher/lower hint logic.
Updated the secret number generation to match the selected difficulty.
Stored the secret number in `st.session_state` so it persists across reruns.
Repaired reset behavior for starting a new game.
Corrected score update behavior.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
![win screenshot](<img/Screenshot 2026-03-14 at 7.35.45 PM.png>)
## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
