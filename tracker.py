"""
tracker.py

I keep the GradeTracker class here. GradeTracker holds every
assignment the user adds and knows how to list, filter, and summarize
them. assignments.py describes a single assignment; this file
manages the whole collection.
"""

# I don't import Homework/Exam here because GradeTracker just stores
# objects that other code creates. That keeps this file focused on
# managing the list of assignments.


class GradeTracker:
    """My GradeTracker holds assignments and provides helper methods.

    I create one GradeTracker in `main.py` and add everything to it.
    """

    def __init__(self):
        # Start with an empty list. I'll store Homework and Exam objects
        # here; they can be mixed because they share the same base class.
        self.assignments = []

    def add_assignment(self, assignment):
        """Add one Homework or Exam to my list and print a message."""
        self.assignments.append(assignment)
        # printing the object uses the Assignment.__str__ formatting
        print(f"\nAdded: {assignment}\n")

    def list_assignments(self, assignments=None):
        """Print a numbered list of assignments.

        If `assignments` is given I print that list; otherwise I print
        everything I have stored in `self.assignments`.
        """
        data = assignments if assignments is not None else self.assignments

        if not data:
            print("\nNo assignments to show.\n")
            return

        print("\n" + "-" * 60)
        # enumerate gives me a number and the item so I can show 1., 2., ...
        for index, item in enumerate(data, start=1):
            print(f"{index}. {item}")
        print("-" * 60 + "\n")

    def filter_assignments(self, atype=None, subject=None, month=None):
        """Return a new list filtered by type, subject, and/or month.

        I don't change the original list; I return a filtered copy so
        the stored data stays safe.
        """
        results = self.assignments

        if atype:
            results = [a for a in results if a.type == atype.lower().strip()]

        if subject:
            results = [a for a in results if a.subject == subject.lower().strip()]

        if month:
            results = [a for a in results if a.due_date.startswith(month.strip())]

        return results

    def show_summary(self):
        """Print overall average, per-subject averages, and high/low.

        If there are no assignments I tell the user and return early.
        """
        if not self.assignments:
            print("\nNo assignments yet, so there is nothing to summarize.\n")
            return

        # overall average
        total_percentage = sum(a.percentage() for a in self.assignments)
        overall_average = total_percentage / len(self.assignments)

        print("\n===== GRADE SUMMARY =====")
        print(f"Overall average: {overall_average:.1f}%")

        # per-subject averages
        subjects = {}
        for a in self.assignments:
            subjects.setdefault(a.subject, []).append(a.percentage())

        print("\nPer-subject averages:")
        for subject, percentages in subjects.items():
            subject_average = sum(percentages) / len(percentages)
            print(f"  {subject.title()}: {subject_average:.1f}%")

        # highest and lowest (compare by percentage)
        highest = max(self.assignments, key=lambda a: a.percentage())
        lowest = min(self.assignments, key=lambda a: a.percentage())

        print(f"\nHighest scoring assignment: {highest}")
        print(f"Lowest scoring assignment:  {lowest}")
        print("==========================\n")
