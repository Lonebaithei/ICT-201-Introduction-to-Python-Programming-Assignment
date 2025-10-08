# SECTION A.1; Student Data Entry

total_students = int(input('Enter the total number of students,' ))

# lists to store student names and grades
student_names = []
student_grades = []

student_count = 1

while student_count <= total_students:

    student_name = str(input(f'Enter student name {student_count},' ))
    # Get grade input from user
    student_grade = float(input(f'Enter student grade {student_count},'))

    print(f'STUDENT {student_count}:{student_name} - GRADE {student_grade}')

    # Add student name to the names list
    student_names.append(student_name)

    # Add student grade to the grades list
    student_grades.append(student_grade)

    student_count += 1

#SECTION A.2; Grade Calculations

total_sum = sum(student_grades)

# Calculate class average by dividing total sum by number of students
class_average = total_sum / total_students

# Display the class average with formatting to 2 decimal places
print(f"\nClass Average: {class_average:.2f}")


print("\nIndividual Student Analysis:")

# Here we should be calculating the average of all the student marks
# Also, after calculating the averages, the code should display the student`s name  alongside their class average mark

# Loop to display performance relative to class average
for i in range(total_students):
    # Calculate how much above or below average the current student is
    difference = student_grades[i] - class_average

    #  performance status based on the difference
    if difference > 0:
        status = "above average"
    elif difference < 0:
        status = "below average"
    else:
        status = "exactly at average"

    # Display individual student's performance
    print(f"{student_names[i]}: {student_grades[i]} ({abs(difference):.2f} points {status})")

    print(f'{total_students} Students have been processed.')
