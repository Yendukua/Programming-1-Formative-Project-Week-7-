each function has ONE clear job.
"""
menu_actions.py

I put the small helper functions for the main menu here. Each function
does one job: ask the user for input, build an object if needed, and
then call the tracker to store or show results.

The functions take `tracker` (a GradeTracker instance) so I can work
with the same list of assignments that `main.py` created.
"""

# I import the data classes I need to create new assignments.
from assignments import Homework, Exam

# I import a helper that checks numbers for me so I don't have to repeat
# the validation logic in every menu function.
from validators import get_valid_score


def add_homework(tracker):
    """I ask the user for homework details and add the homework to the
    tracker. I keep the function small so it's easy to read.
    """
    print("\n--- Add Homework ---")
    subject = input("Subject: ")
    title = input("Title: ")

    # I use get_valid_score() so the input is already a valid number.
    score = get_valid_score("Score: ")
    max_score = get_valid_score("Max score: ")

    # I make sure the score is not greater than the max score.
    if score > max_score:
        print("A score cannot be greater than the max score. Homework was not added.\n")
        return

    due_date = input("Due date (YYYY-MM-DD): ")

    # I create a Homework object and give it to the tracker to store.
    homework = Homework(subject, title, score, max_score, due_date)
    tracker.add_assignment(homework)


def add_exam(tracker):
    """I ask for exam details (like add_homework) and add an Exam to the
    tracker.
    """
    print("\n--- Add Exam ---")
    subject = input("Subject: ")
    title = input("Title: ")
    score = get_valid_score("Score: ")
    max_score = get_valid_score("Max score: ")

    # Same check as homework: score must not exceed max score.
    if score > max_score:
        print("A score cannot be greater than the max score. Exam was not added.\n")
        return

    due_date = input("Due date (YYYY-MM-DD): ")
    exam = Exam(subject, title, score, max_score, due_date)
    tracker.add_assignment(exam)


def filter_menu(tracker):
    """I show a small filter menu, ask what the user wants to filter by,
    then show the matching results.
    """
    print("\n--- Filter Assignments ---")
    print("1) By subject")
    print("2) By type (homework/exam)")
    print("3) By month (e.g. 2025-10)")
    sub_choice = input("Choose an option: ").strip()

    # Depending on the choice, I ask for a different value and call the
    # tracker's filter method. I store the results and then reuse the
    # tracker's list_assignments() to print them.
    if sub_choice == "1":
        subject = input("Enter subject: ")
        results = tracker.filter_assignments(subject=subject)
    elif sub_choice == "2":
        atype = input("Enter type (homework/exam): ")
        results = tracker.filter_assignments(atype=atype)
    elif sub_choice == "3":
        month = input("Enter month (YYYY-MM): ")
        results = tracker.filter_assignments(month=month)
    else:
        print("That is not a valid filter option.")
        return

    tracker.list_assignments(results)
