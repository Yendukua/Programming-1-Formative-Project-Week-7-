"""
main.py

This is the file I run to start the program (python3 main.py).

I kept most code in other files so this file only shows the menu and
calls functions. That makes it easier to read and change later.
"""

# I use GradeTracker to store and work with assignments.
from tracker import GradeTracker

# get_menu_choice() asks the user for a menu number and checks it.
#from validators import get_menu_choice

# The menu action functions do the work for options 1, 2 and 4.
#from menu_actions import add_homework, add_exam, filter_menu


def main():
    # I make one GradeTracker and use it for the whole program.
    tracker = GradeTracker()

    print("=== Student Grade / Assignment Tracker ===")

    running = True
    # Keep showing the menu until I set running = False
    while running:
        # show the menu
        print("\n1) Add homework")
        print("2) Add exam")
        print("3) List assignments")
        print("4) Filter (by subject / type / month)")
        print("5) Show summary")
        print("0) Exit")

        # get_menu_choice() will keep asking until the user types a valid option
        #choice = get_menu_choice()

        # route the choice to the right place
        if choice == "1":
            # call the function that asks for homework details and adds it
            add_homework(tracker)
        elif choice == "2":
            # call the function that asks for exam details and adds it
            add_exam(tracker)
        elif choice == "3":
            # I can list assignments directly from the tracker object
            tracker.list_assignments()
        elif choice == "4":
            # filter_menu handles asking what filter to use and shows results
            filter_menu(tracker)
        elif choice == "5":
            # show a summary of grades
            tracker.show_summary()
        elif choice == "0":
            # user asked to quit - say bye and stop the loop
            print("\nGoodbye! Thanks for using the Grade Tracker.")
            running = False


# I only run main() when this file is run directly. That lets me import
# functions from this file in tests or other programs without starting
# the menu automatically.
if __name__ == "__main__":
    main()
