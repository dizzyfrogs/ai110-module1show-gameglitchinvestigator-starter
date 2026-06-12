# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guessed 50 | Too Low hint | Too High hint | None |
| Hard difficulty | Guess from 1-100 | Difficulty was ignored | None |
| Started New Game | Reset score & history | Did not reset | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude Code (Sonnet 4.6) on this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

Claude found that the hint messaages in `check_guess` were inverted. So, when a guess was too high, the message said to go higher instead of lower. I verified this by reading the logic directly. It was an easy fix.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Claude flagged that the win score formula was incorrect, but I felt that was a matter of design choice and not necessarily a bug. That is a bit ambiguous.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

First I read the code and reasoned through it. Some of the bugs are plainly visible. Second, running a targeted pytest case for each fix before committing. If the test failed before the fix it would've been a stronger verification, but at minimum each new test cofirmed the corrected behavior.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I manally tested the higher/lower logic by playing the game and watching the hint messages in the UI. I used the Developer Debug info section to see the secret number while guessing, which let me directly compare the hint to what it should say. When my guess was above the secret, the game told me to go higher. That confirmed the messages were reversed.

- Did AI help you design or understand any tests? How?

Yes, almost entirely. Claude wrote every new test in this session. It also helped me understand what each test should be checking. For example, for the hint message bug, I knew I wanted to verify the direction was correct, but Claude helped me see that check_guess returns a tuple, so the assertion needed to unpack `outcome, _ = check_guess(...)` instead of just comparing the whole return value directly.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Every time you interact with a Streamlit app, it reruns the entire Python script from top to bottom. It's not like a normal site where only one part updates. It re-executes the whole file. So any regular variable you set gets wiped out on the next interaction. Session state is how you keep info alve across the reruns. It's a dict that Streamlit preserves between runs.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

Committing after each individual bug fix rather than all at once. It kept the git history readable and kept the commits focused. If something broke later, I could pinpoint exactly which change caused it instead of searching through a large diff.

- What is one thing you would do differently next time you work with AI on a coding task?

Run existing tests before writing new ones. I assumed the pre-existing tests worked ot of the box, but they were already borken.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

I came in thinking AI-generated code would either work or obviously not work. I didn't expect code that ran fine, looked reasonable, and still contained small logic errors.. AI output needs to be reviewed just like human-made code.
