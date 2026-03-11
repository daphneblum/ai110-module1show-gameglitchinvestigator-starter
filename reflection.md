# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
Game played normally, seemed to be working
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1.The hints were incorrect, kept telling me to guess lower no matter what I input. I expected it to tell me higher or lower based on my guesses. For example, it said "lower" even when I guessed 1, when the secret number was between 1 and 100 and ended up being 83.

  2.On easy mode, the secret number was supposed to be between 1 and 20 but ended up being 40. Again it kept telling me to guess lower despite the number being above the supposed range.

  3.I expected the new game button to restart the game, but it did nothing.

  4.The score given is negative, even if you win

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude Code on this project. 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

Claude found that the feedback messages were inverted and that on even-numbered attempts, the secret number was being converted to a string, thus raising a type error. I verified it but I checking the code it wanted to edit to verify what is said, as well as testing out the game afterwards to ensure the edits solved the issue.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

An incorrect suggestion was when fixing the reset button. When first starting up the game and switching to easy, it says five attempts left. When you reset the game, it changes the label to say six attempts. Then it gives a game over when you use five attempts, while still saying one attempt left.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
