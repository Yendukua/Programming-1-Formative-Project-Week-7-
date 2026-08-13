# Student Grade & Assignment Tracker

I built a small command-line Python app to track homework and exam
results, filter entries, and show simple grade summaries. Data is
stored only in memory for the current session.

Usage
-----
1. Clone the repo:
  ```
  git clone https://github.com/Yendukua/Programming-1-Formative-Project-Week-7-.git
  cd Programming-1-Formative-Project-Week-7-
  ```
2. Run:
  ```
  python3 main.py
  ```

What it does
-----------
- Add homework and exam entries (subject, title, score, max score, due date)
- List and filter assignments (by subject, type, or month)
- Show overall and per-subject averages
- Basic input validation for scores and menu choices

Project layout
--------------
- `main.py` — entry point and menu loop
- `assignments.py` — `Assignment`, `Homework`, `Exam`
- `tracker.py` — `GradeTracker` for storing and summarizing data
- `validators.py` — input helpers
- `menu_actions.py` — menu handlers

Notes
-----
- No external libraries required.
- Keep all files together so imports work.

If you want the README even shorter or to change the tone, tell me how you write and I'll adjust it.
