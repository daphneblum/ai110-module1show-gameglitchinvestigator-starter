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

I would run the game multiple times, checking for various cases.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  
  One test was switching between difficulty modes, where I realized the game was not resetting the secret number for other modes. For example, it would set the number for normal mode, which was between 1 and 100, but when you switched to easy mode, which was supposed to be 1 to 20, it would not change the secret number to be one in that range. This told me there was a bug regarding the score when the game mode was changed.

- Did AI help you design or understand any tests? How?
Yes, Claude Code was used to explain what logic was causing the bugs and why they were failing the tests.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

Unfortunately, I never actually saw that bug! I did not realize we could see what the secret number was in the Developer Debug Info until after I had already began working on bugs because the first one I noticed was when trying the game and seeing that the secret number was above the range in the easy mode. Because of this, I seem to have indirectly fixed that bug and therefore am not sure which specific change I made to give a stable secret number. However, the bug likely happened because the secret number was being regenerated each time the script reran instead of being stored in session state.

Streamlit reruns re-execute the script from the beginning to the end. Session state stores variables between reruns.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  One habit I would reuse is testing the program after each change instead of making multiple edits at once. Running the game repeatedly helped me confirm whether a fix actually worked and helped reveal other issues, such as problems when switching between difficulty modes. This made it easier to isolate which changes were solving which bugs.

- What is one thing you would do differently next time you work with AI on a coding task?

Next time I would verify AI suggestions more carefully before implementing them. Some of the suggestions from Claude were helpful, but others introduced new issues or misunderstood how the program logic worked. I found that reading the code myself and testing changes step by step was important for confirming whether the suggestion was actually correct.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project reinforced that AI can be useful for identifying possible issues, but its suggestions still need to be verified carefully. It works best as a debugging assistant rather than something that can reliably fix problems without review.