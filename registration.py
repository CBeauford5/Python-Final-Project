# ----------------------------------------------------------------
# Author: Thomas Reaves
# Date: April 18, 2022.
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for. It also allows students to review the tuition
# # costs for their course roster.
# -----------------------------------------------------------------
import billing
import student


def main():
    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, in_state_list, course
    # list, max class size list and roster list.  It uses a loop to
    # serve multiple students. Inside the loop, ask student to enter
    # ID, and call the login function to verify student's identity.
    # Then let student choose to add course, drop course or list
    # courses. This function has no return value.
    # -------------------------------------------------------------

    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444')]
    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False}

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': []}
    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}

    student_id = ''
    while student_id != '0':        # Login Credential Loop
        student_id = input("Enter ID to log in, or 0 to quit: ")
        if student_id == '0':
            quit()
        else:
            validation = login(student_id, student_list)    # Calls login function

            if validation:
                choice = input(
                        "Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: ")
                while choice not in ['0', '1', '2', '3', '4']:     # Initial Input Validation
                    print('Please enter 0, 1, 2, 3, or 4.')
                    print('')
                    choice = input(
                        "Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: ")

                while choice in ['0', '1', '2', '3', '4']:         # Menu Loop
                    if choice == '1':
                        student.add_course(student_id, course_roster, course_max_size)    # Calls add_course function
                        choice = input(
                            "Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: ")
                        while choice not in ['0', '1', '2', '3', '4']:    # Input Validation
                            print('Please enter 0, 1, 2, 3, or 4.')
                            print('')
                            choice = input(
                                "Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: ")

                    elif choice == '2':
                        student.drop_course(student_id, course_roster)     # Calls drop_course function
                        choice = input(
                            "Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: ")
                        while choice not in ['0', '1', '2', '3', '4']:     # Input Validation
                            print('Please enter 0, 1, 2, 3, or 4.')
                            print('')
                            choice = input(
                                "Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: ")

                    elif choice == '3':
                        student.list_courses(student_id, course_roster)    # Calls list_courses function
                        choice = input(
                            "Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: ")
                        while choice not in ['0', '1', '2', '3', '4']:     # Input Validation
                            print('Please enter 0, 1, 2, 3, or 4.')
                            print('')
                            choice = input(
                                "Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: ")

                    elif choice == '4':
                        hours, cost = billing.calculate_hours_and_bill(student_id, student_in_state, course_roster,
                                                                       course_hours)
                        billing.display_hours_and_bill(hours, cost)    # Calls billing functions
                        choice = input(
                            "Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: ")
                        while choice not in ['0', '1', '2', '3', '4']:       # Input Validation
                            print('Please enter 0, 1, 2, 3, or 4.')
                            print('')
                            choice = input(
                                "Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: ")

                    else:                                              # Ends current student's session
                        print("Session ended.")
                        print('')
                        break


def login(student_id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------
    pin = input("Enter PIN: ")

    if (student_id, pin) in s_list:         # Login Credential Validation
        print("ID and PIN verified")
        print('')
        return True
    else:
        print("ID or PIN incorrect")
        print('')
        return False


main()
