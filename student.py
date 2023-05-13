# ----------------------------------------------------------------
# Mary Benson
# April 18th, 2022
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------


def add_course(student_id, c_roster, c_max_size):
    # ------------------------------------------------------------
    # This function adds a student to a course.  It has three
    # parameters: id is the ID of the student to be added; c_roster is the
    # list of class rosters; c_max_size is the list of maximum class sizes.
    # This function asks user to enter the course he/she wants to add.
    # If the course is not offered, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.
    # If the course is full, display error message and stop.
    # If everything is okay, add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------

    course = input('Enter course you want to add: ')

    if course not in c_roster:                             # Course validation
        print('Course not found.')
        print('')
    elif student_id in c_roster[course]:
        print('You are already enrolled in that course.')
        print('')
    elif len(c_roster[course]) == c_max_size[course]:
        print('Course already full.')
        print('')
    else:                                                  # Course Added
        c_roster[course].append(student_id)
        print('Course added.')
        print('')


def drop_course(student_id, c_roster):
    # ------------------------------------------------------------
    # This function drops a student from a course.  It has two
    # parameters: id is the ID of the student to be dropped;
    # c_roster is the list of class rosters. This function asks
    # the user to enter the course he/she wants to drop.  If the course
    # is not offered, display error message and stop.  If the student
    # is not enrolled in that course, display error message and stop.
    # Remove student ID from the course’s roster and display a message
    # if there is no problem.  This function has no return value.
    # -------------------------------------------------------------

    course = input('Enter course you want to drop: ')

    if course not in c_roster:                              # Course Validation
        print('Course not found.')
        print('')
    elif student_id not in c_roster[course]:
        print('You are not enrolled in that course.')
        print('')
    else:                                                   # Course Dropped
        c_roster[course].remove(student_id)
        print('Course dropped')
        print('')


def list_courses(student_id, c_roster):
    # ------------------------------------------------------------
    # This function displays and counts courses a student has
    # registered for.  It has two parameters: id is the ID of the
    # student; c_roster is the list of class rosters. This function
    # has no return value.
    # -------------------------------------------------------------

    print('Courses registered:')                            # Displays student's courses and the number of courses
    count = 0
    for key in c_roster.keys():
        if student_id in c_roster[key]:
            print(key)
            count += 1
    print(f'Total number: {count}')
    print('')
