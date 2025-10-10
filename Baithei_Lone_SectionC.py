# subjects taken by each student
subjects = ["Math", "English", "Science"]  
num_subjects = len(subjects)  # Get the number of subjects

total_students = int(input('Enter the total number of students,' ))

# student record dictionary (name: {subject: grade})
student_records = {}

# counter to track current student
student_count = 1

# Loop through each student that needs to be processed
while student_count <= total_students:

    student_name = input(f"\nEntry for student {student_count}: ")

    # Use a dictionary to store grades for subjects for the current student
    student_grades = {}

    print(f"Entering grades for {student_name}:")

    # A Loop to get grades for subjects
    for subject in subjects:
        while True:
            try:
                grade_input = input(f"  Enter {subject} grade (0-100): ")

                grade = float(grade_input)

                if grade < 0 or grade > 100:
                    print("  Error: Grade must be between 0 and 100. Please try again.")
                    # Continue loop to call for grade
                    continue
                # Break if input is valid
                break

            except ValueError:
                print("  Invalid input! Please enter a grade between (0-100)") # Corrected prompt

        # Add grade to current student's grade dictionary
        student_grades[subject] = grade

    # Add the student's grades dictionary to the main student_records dictionary
    student_records[student_name] = student_grades

    # Display confirmation message with entered data
    print(f"Processed {student_name} with grades: {student_grades}")

    # Increment counter to move to next student
    student_count += 1

# The following code for calculating averages, subject analysis, and summaries will be updated
# in subsequent steps to work with the new dictionary structure.
# For now, we just focus on refactoring the data structure.

# Calculating and displaying average grade for every student
# print("\n----Student Average Grades----")
# for student_name, student_grades in student_records:
#     average_grade = sum(student_grades.values()) / len(student_grades) # Updated to use dict.values()
#     print(f"{student_name}: Average Grade = {average_grade:.2f}")

#     # Determine and print the highest and lowest grade for each subject
# print("\n--- Subject Grade Analysis ---")

# # Initialize dictionaries to store grades for each subject across all students
# subject_grades_dict = {subject: [] for subject in subjects} # Updated to use a dictionary

# for student_name, student_grades in student_records.items(): # Updated to use dict.items()
#     for subject, grade in student_grades.items(): # Updated to use dict.items()
#         subject_grades_dict[subject].append(grade)

# for subject in subjects:
#     highest_grade = max(subject_grades_dict[subject])
#     lowest_grade = min(subject_grades_dict[subject])
#     print(f"{subject}: Highest Grade = {highest_grade:.2f}, Lowest Grade = {lowest_grade:.2f}")

#     # A summary displaying student`s report
# print("\n--- Student Summary ---")
# for student_name, student_grades in student_records.items(): # Updated to use dict.items()
#     average_grade = sum(student_grades.values()) / len(student_grades) # Updated to use dict.values()
#     print(f"Name: {student_name}")
#     print(f"  Grades: {student_grades}")
#     print(f"  Average Grade: {average_grade:.2f}")
#     print("-" * 20) # Separator for readability