# Global list for storing student data
# Each student is represented by a dictionary with the keys "name" and "grades"

students = []


def student_exist(student_name:str)->bool:
    """
    Checks if a student with the given name exists.
    :param student_name: Student name to check
    :return: True if the student exists, False otherwise
    """
    for student in students:
        if student["name"] == student_name:
            return True

    return False


def create_student_grades_list()->list:
    """
    Creates a list of student grades based on user input.
    :return: List of integers from 0 to 100 representing ratings
    """
    new_grades = []
    while True:
        user_input = input("Enter a grade or 'done' for finish: ").lower()

        if user_input == "done":
            break
        try:
            student_grade = int(user_input)
            if student_grade in [int(i) for i in range(0, 101)]:
                new_grades.append(student_grade)
            else:
                print(f"Error: Student's grade must be between 0 and 100!")

        except ValueError:
            print(f"Error: Invalid input! Please enter a number.")

    return new_grades


def protect_empty_stabs(students_data:list):
    """
    Checks that the student list is not empty and that each student has a name and grades.
    :param students_data: List of student data
    :return: True if the data is valid, False otherwise
    """
    if len(students_data)==0:
        return False

    for student_data in students_data:
        if len(student_data["name"]) == 0 or len(student_data["grades"])==0:
            return False
    return True


def count_average_grade(grades:list)->float:
    """
    Calculates the average grades from a list of ratings.
    :param grades:List of grades
    :return: Average rating
    """
    average_grade = round(sum(grades)/len(grades),1)
    return average_grade


def create_names_list(students_data:list)->list:
    """
    Creates a list of all student names.
    :param students_data: List of student data
    :return: List of student names
    """
    names = []

    for student_data in students_data:
        for key in student_data.keys():
            if key == "name":
                names.append(student_data[key])

    return names


def create_removed_na_names_list(students_data: list) -> list:
    """
    Creates a list of names of students who have numeric grades (not "N/A").
    :param students_data: List of student data
    :return: List of names of students with valid grades
    """
    names = []

    for student_data in students_data:
        if student_data["grades"]!=["N/A"]:
            names.append(student_data["name"])

    return names


def create_average_grades_list(students_data:list)->list:
    """
    Creates a list of average grades for each student.
    :param students_data: List of student data
    :return: List of average ratings or "N/A" if there are no ratings
    """
    grades = []

    for student_data in students_data:
        try:
            for key, value in student_data.items():
                if key=="grades" and isinstance(value,list):
                    avg_grade = count_average_grade(value)
                    grades.append(avg_grade)
        except ZeroDivisionError:
            grades.append("N/A")

    return grades


def remove_na_values(average_grades:list)->list:
    """
    Removes "N/A" values from the list of average ratings.
    :param average_grades: List of average grades
    :return: List of numerical average ratings
    """
    return [float(average_grade) for average_grade in average_grades if average_grade!="N/A"]


def create_average_grades_consolidated_report(names:list, average_grades:list)->str:
    """
    Creates a consolidated report with student names and average grades.
    :param names: List of student names
    :param average_grades: List of average ratings
    :return: Formatted text
    """
    report = '\n'.join([
        f"{name}'s average grade is {average_grade}."
        for name, average_grade in zip(names, average_grades)
    ])

    return report


def create_average_grades_general_report(removed_na_values:list)->str:
    """
    Creates a summary report with the maximum, minimum, and overall average score.
    :param removed_na_values: List of numerical average ratings
    :return: Formatted text
    """
    return (f"Max Average: {max(removed_na_values)}.\n"
            f"Min Average: {min(removed_na_values)}.\n"
            f"Overall Average: {count_average_grade(removed_na_values)}.\n")


def create_general_average_grades(names:list, avg_grades:list)->list:
    """
    Creates a list of tuples (name, average).
    :param names: List of student names
    :param avg_grades: List of average ratings
    :return: List of tuples (name, average).
    """
    general_average_grades = [tuple(general_average_grade) for general_average_grade in
                              tuple(zip(names, avg_grades))]

    return general_average_grades


def create_new_student()->str:
    """
    Creates a new student and adds it to the global list.
    :return: Message about the result of the operation
    """
    name = input("Enter student name: ").title()

    if student_exist(name):
        return f"Error: Student {name} already exists!"

    students.append({"name":name, "grades":[]})
    return f"Student {name} was added successfully!"


def add_student_grade():
    """
    Adds grades for an existing student.
    :return: Message about the result of the operation
    """
    name = input("Enter student name: ").title()

    if not student_exist(name):
        return f"Error: Student {name} doesn't exist!"

    student_grades = create_student_grades_list()

    if len(student_grades) == 0:
        return f"No grades have been added to student {name}!"

    for student in students:
        if student["name"] == name:
            student["grades"].extend(student_grades)

    return (f"Student {name}'s grades ({', '.join(map(str, student_grades))})"
            f" have been successfully added!")


def show_report():
    """
    Shows a full report on all students.
    :return: Formatted report with detailed information
    """
    if protect_empty_stabs(students):
        students_names = create_names_list(students)
        average_students_grades = create_average_grades_list(students)
    else:
        return "Either the student's name or grades were not added."

    clean_average_students_grades = remove_na_values(average_students_grades)

    consolidated_report = create_average_grades_consolidated_report(students_names,average_students_grades)
    general_report = create_average_grades_general_report(clean_average_students_grades)

    return (f"---Student report---\n"
            f"{consolidated_report}\n"
            f"{'-'*30}\n"
            f"{general_report}")


def find_top_performer():
    """
    Finds the student with the highest grade point average.
    :return: Message with information about the best student
    """
    if protect_empty_stabs(students):
        removed_na_names = create_removed_na_names_list(students)
        average_students_grades = create_average_grades_list(students)
    else:
        return "Either the student's name or grades were not added."

    general_average_grades = create_general_average_grades(removed_na_names, average_students_grades)


    max_average_grade = max(general_average_grades, key=lambda x: x[1])

    return (f"The student with the highest average is {max_average_grade[0]} "
            f"with a grade {max_average_grade[1]}.")



def menu():
    """
    The menu's primary function is for user interaction.
    Provides an interface for managing the student accounting system.
    :return:
    """
    menu_options = [
        "Add a new student",
        "Add a grades for a student",
        "Show report (all students)",
        "Find top performer",
        "Exit"
    ]


    while True:

        for index, menu_option in enumerate(menu_options):
            print(index + 1, menu_option)

        try:
            user_input = int(input("Enter your choice: "))

            if user_input == 1:
                result = create_new_student()
                print(result)

            elif user_input == 2:
                result = add_student_grade()
                print(result)

            elif user_input == 3:
                result = show_report()
                print(result)

            elif user_input == 4:
                result = find_top_performer()
                print(result)

            elif user_input == 5:
                print("Exiting program.")
                break
            else:
                print("You entered a wrong number. Please try again.")

        except ValueError:
            return "You entered a non-existent command. Please try again."


if __name__== "__main__":
    menu()




















