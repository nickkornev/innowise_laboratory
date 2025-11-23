students = []

def create_new_student()->str:
    name = input("Enter student name: ").capitalize()

    for student in students:
        if student["name"] == name:
            return f"Error: Student {name} already exists!"

    student_info = {"name":name, "grades":[]}
    students.append(student_info)

    return f"Student {name} was added successfully!"


def add_student_grade()->str:
    student_grades = []
    name = input("Enter student name: ").capitalize()

    student_exists = False
    for student in students:
        if student["name"]==name:
            student_exists = True
            break

    if not student_exists:
        return f"Student {name} doesn't exist!"

    for student in students:
        if student["name"]==name:
            while True:
                student_input = input("Enter a grade or 'done' for finish: ").lower()
                if student_input == "done":
                        break
                try:
                    student_grade = int(student_input)
                    if student_grade in [int(i) for i in range(0,101)]:
                        student_grades.append(student_grade)
                    else:
                        print(f"Error: Student's grade must be between 0 and 100!")

                except ValueError:
                    print(f"Error: Invalid input! Please enter a number.")
                continue

    for student in students:
        if student["name"] == name:
            student["grades"] = student_grades
            if len(student_grades)==0:
                return f"No grades have been added to student {name}!"

    return (f"Student {name}'s grades ({', '.join(map(str,student_grades))})"
            f" have been successfully added!")


def show_report()->str:
    students_names = []
    average_students_grades = []

    for student in students:
        if len(student["name"]) == 0 or len(student["grades"]) == 0:
            return "Either the student's name or grades were not added."

    for student in students:
        if len(student["name"])!=0 or len(student["grades"])!=0:
            try:
                for key,value in student.items():
                    if key == "name":
                        students_names.append(value)
                    else:
                        average_students_grades.append(round(sum(value)/len(value),1))
            except ZeroDivisionError:
                average_students_grades.append("N/A")

    reports='\n'.join([
        f"{student_name}'s average grade is {average_student_grade}."
        for student_name, average_student_grade in zip(students_names, average_students_grades)
    ])

    cleaned_average_grades = []
    for average_students_grade in average_students_grades:
        while average_students_grade!="N/A":
            cleaned_average_grades.append(average_students_grade)
            break

    report_final_lines = (f"Max Average: {max(cleaned_average_grades)}.\n"
                   f"Min Average: {min(cleaned_average_grades)}.\n"
                   f"Overall Average: {round(sum(cleaned_average_grades)/len(cleaned_average_grades),1)}."
                          )

    return (f"---Student report---\n"
            f"{reports}\n"
            f"{'-'*30}\n"
            f"{report_final_lines}")


def find_top_performer():
    students_names = []
    average_students_grades = []
    skipped_students_names = []

    for student in students:
        if len(student["name"])==0 or len(student["grades"])==0:
            return "Either the student's name or grades were not added."

    for student in students:
        if len(student)!=0 and len(student["grades"])!=0:
            students_names.append(student["name"])
            average_students_grades.append(round(sum(student["grades"])/len(student["grades"]),1))
        else:
            skipped_students_names.append(student["name"])

    general_average_grades = [tuple(general_average_grade) for general_average_grade in
                              tuple(zip(students_names,average_students_grades))]
    max_average_grade = max(general_average_grades, key=lambda x:x[1])

    return (f"The student with the highest average is {max_average_grade[0]} "
            f"with a grade {max_average_grade[1]}.")


def menu():
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
    end_result = menu()
    print(end_result)




















