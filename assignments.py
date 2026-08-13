"""
assignments.py

I define what an assignment is here. I made a base `Assignment`
class and two subclasses: `Homework` and `Exam`. Other files import
these classes to create assignments without knowing the details.
"""


class Assignment:
    """Base class for a single assignment.

    I store subject, title, score, max_score, due_date and type here.
    Homework and Exam inherit from this so they don't have to repeat
    the same code.
    """

    def __init__(self, subject, title, score, max_score, due_date, atype):
        # __init__ runs when I create a new assignment object. "self"
        # is the object I'm building so I save values on it.

        # Normalize the subject so filtering works even if the user
        # types different case or extra spaces.
        self.subject = subject.lower().strip()
        self.title = title.strip()

        # Convert scores to floats so I can calculate percentages.
        self.score = float(score)
        self.max_score = float(max_score)

        self.due_date = due_date.strip()

        # type is set by the subclasses (homework or exam).
        self.type = atype

    def percentage(self):
        """Return score as a percentage (0-100).

        I guard against division by zero and return 0 if max_score is 0.
        """
        if self.max_score == 0:
            return 0
        return (self.score / self.max_score) * 100

    def __str__(self):
        # __str__ returns a readable string when I print the object.
        # :.1f formats the percentage with one decimal place (e.g. 80.0).
        return (f"[{self.type.upper()}] {self.subject.title()} - {self.title} | "
                f"{self.score}/{self.max_score} ({self.percentage():.1f}%) | "
                f"Due: {self.due_date}")


class Homework(Assignment):
    """Homework class - a simple subclass of Assignment.

    I inherit from Assignment so I reuse its methods and only set the
    type to "homework".
    """

    def __init__(self, subject, title, score, max_score, due_date):
        # Call the parent initializer to set common fields and set type
        # to "homework" so callers don't need to provide it.
        super().__init__(subject, title, score, max_score, due_date, "homework")


class Exam(Assignment):
    """Exam class - like Homework but type is "exam"."""

    def __init__(self, subject, title, score, max_score, due_date):
        super().__init__(subject, title, score, max_score, due_date, "exam")
