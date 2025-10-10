# subjects that will be graded for each student
subjects = ["Math", "English", "Science"]  # List of subject names
num_subjects = len(subjects)  # Get the number of subjects

total_students = int(input('Enter the total number of students,' ))

# this is an empty list to store student records (name, grades)
student_records = []  # List of tuples: (student_name, [grade1, grade2, grade3])

# counter to track current student
student_count = 1

# Loop through each student that needs to be processed
while student_count <= total_students:
    # Get current student's name from user input
    student_name = input(f"\nEnter name for student {student_count}: ")

    student_grades = []  # List to store grades for all subjects

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
                print("  Invalid input! Please enter a grade between (0-10)")

        # Add grade to current student's grade list
        student_grades.append(grade)

    # Create a tuple
    student_record = (student_name, student_grades)
    student_records.append(student_record)  # Add tuple to main records list

    # Display confirmation message with entered data
    print(f"Processed {student_name} with grades: {student_grades}")

    # Increment counter to move to next student
    student_count += 1

    # Calculating and displaying average grade for every student
print("\n----Student Average Grades----")
for student_name, student_grades in student_records:
    average_grade = sum(student_grades) / len(student_grades)
    print(f"{student_name}: Average Grade = {average_grade:.2f}")

    # Determine and print the highest and lowest grade for each subject
print("\n--- Subject Grade Analysis ---")

# Initialize lists to store grades for each subject across all students
subject_grades_list = [[] for _ in range(num_subjects)]

for student_name, student_grades in student_records:
    for i in range(num_subjects):
        subject_grades_list[i].append(student_grades[i])

for i in range(num_subjects):
    subject_name = subjects[i]
    highest_grade = max(subject_grades_list[i])
    lowest_grade = min(subject_grades_list[i])
    print(f"{subject_name}: Highest Grade = {highest_grade:.2f}, Lowest Grade = {lowest_grade:.2f}")

    # A summary displaying student`report
print("\n--- Student Summary ---")
for student_name, student_grades in student_records:
    average_grade = sum(student_grades) / len(student_grades)
    print(f"Name: {student_name}")
    print(f"  Grades: {student_grades}")
    print(f"  Average Grade: {average_grade:.2f}")
    print("-" * 20) # Separator for readability
