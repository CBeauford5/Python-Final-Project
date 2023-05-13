# ----------------------------------------------------------------
# Author: Hyppolite Mavungu
# Date: April 18, 2022.
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------


def calculate_hours_and_bill(student_id, s_in_state, c_rosters, c_hours):
    # ------------------------------------------------------------
    # This function calculate billing information. It takes four
    # parameters: id, the student id; s_in_state, the list of
    # in-state students; c_rosters, the rosters of students in
    # each course; c_hours, the number of hours in each course.
    # This function returns the number of course hours and tuition
    # cost.
    # ------------------------------------------------------------

    if s_in_state[student_id]:                       # Sets cost and accumulates credit hours for in-state student
        cost = 225.00
        hours = 0
        for key in c_rosters.keys():
            if student_id in c_rosters[key]:
                hours += c_hours[key]

        return hours, cost

    else:                                            # Sets cost and accumulates credit hours for out of state student
        cost = 850.00
        hours = 0
        for key in c_rosters.keys():
            if student_id in c_rosters[key]:
                hours += c_hours[key]

        return hours, cost


def display_hours_and_bill(hours, cost):                    # Displays course load and total enrollment cost
    # ------------------------------------------------------------
    # This function prints the number of course hours the student
    # is taking and the total tuition cost. It takes two parameters:
    # hours and cost. This function has no return value.
    # ------------------------------------------------------------
    print(f'Course load: {hours} credit hours')
    print(f'Enrollment cost: ${cost * hours:.2f}')
    print('')
