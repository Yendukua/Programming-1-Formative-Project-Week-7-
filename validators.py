"""
validators.py

I put small helper functions here that ask the user for input and make
sure the input is safe before the rest of the program uses it. I did
this so the program won't crash if I or someone else types the wrong
thing (like letters when a number is expected).

Other files (like `menu_actions.py` and `main.py`) import these
functions so I don't have to copy the same checks everywhere.
"""


def get_valid_score(prompt):
    """I keep asking until the user types a valid non-negative number.

    I return the value as a float. `prompt` is shown to the user
    (for example: "Score: ").
    """
    while True:
        raw_value = input(prompt).strip()

        # I try to convert the text to a number. If it fails, I ask
        # again instead of letting the program crash.
        try:
            number = float(raw_value)
        except ValueError:
            print("That is not a valid number. Please try again.")
            continue

        # I don't accept negative scores.
        if number < 0:
            print("A score cannot be negative. Please try again.")
            continue

        # The input looks good, so I return it.
        return number


def get_menu_choice():
    """I ask the user for the main-menu number and only accept 0-5.

    I return the chosen option as a string so the caller can compare it
    directly to the menu labels.
    """
    valid_choices = ["0", "1", "2", "3", "4", "5"]
    choice = input("\nEnter your choice: ").strip()

    # If the user types something not in the list, I keep asking.
    while choice not in valid_choices:
        print("Invalid choice. Please enter a number between 0 and 5.")
        choice = input("Enter your choice: ").strip()

    return choice


def get_valid_date(prompt):
    """Keep asking until the user types a valid date in YYYY-MM-DD.

    Returns the string as entered (striped). The function validates
    year/month/day values (including leap years) using datetime.
    """
    import datetime
    import re

    pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    while True:
        raw_value = input(prompt).strip()

        # Quick format check: exactly YYYY-MM-DD with digits.
        if not pattern.match(raw_value):
            print("Invalid format. Please use YYYY-MM-DD (e.g. 2025-10-31).")
            continue

        # Parse numeric components and validate real calendar date.
        try:
            year_s, month_s, day_s = raw_value.split("-")
            year = int(year_s)
            month = int(month_s)
            day = int(day_s)
        except ValueError:
            print("Invalid date components. Use numbers for year, month and day.")
            continue

        try:
            datetime.date(year, month, day)
        except ValueError:
            print("Invalid date. Please ensure the month/day are valid (e.g. not day 33).")
            continue

        return raw_value


def get_valid_month(prompt):
    """Ask until the user provides a valid month in YYYY-MM.

    Ensures the format is numeric and the month is between 01 and 12.
    Returns the entered string (stripped).
    """
    import re

    pattern = re.compile(r"^\d{4}-\d{2}$")

    while True:
        raw_value = input(prompt).strip()

        if not pattern.match(raw_value):
            print("Invalid format. Please use YYYY-MM (e.g. 2025-10).")
            continue

        try:
            _, month_s = raw_value.split("-")
            month = int(month_s)
        except ValueError:
            print("Invalid month. Use numbers for year and month.")
            continue

        if not (1 <= month <= 12):
            print("Invalid month. Month must be between 01 and 12.")
            continue

        return raw_value
