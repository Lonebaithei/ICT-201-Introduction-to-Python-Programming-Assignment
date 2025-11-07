# Comprehensive Grading System - Section A: Scalar Objects and Loops
# This program handles basic student data entry, grade calculations, and input validation

def main():
    """Main function to run the grading system"""
    
    # Display program header
    print("=" * 50)
    print("    COMPREHENSIVE GRADING SYSTEM")
    print("=" * 50)
    
    # 1. STUDENT DATA ENTRY
    # Get the number of students with validation
    num_students = get_number_of_students()
    
    student_names = []  
    student_grades = [] 
    
    process_student_data(num_students, student_names, student_grades)
    
    total_grade, average_grade = calculate_grades(student_grades)
    
    display_results(student_names, student_grades, total_grade, average_grade, num_students)

def get_number_of_students():
    """
    Get and validate the number of students in the class
    Returns: validated number of students (integer)
    """
    while True:
        try:
            # Prompt user to enter number of students
            num_students = int(input("\nEnter the number of students in the class: "))
            
            # Validate that the number is positive
            if num_students <= 0:
                print(" Please enter a positive number of students.")
                continue
                
            # Return valid number of students
            return num_students
            
        except ValueError:
            # Handle non-integer input
            print(" Invalid input! Please enter a valid number.")

def get_student_grade(student_number):
    """
    Get and validate a single student's grade
    Args: student_number - current student being processed
    Returns: validated grade (float)
    """
    while True:
        try:
            # Prompt user for grade input
            grade_input = input(f"Enter grade for student {student_number} (0-100): ")
            
            # Convert input to float
            grade = float(grade_input)
            
            # Validate grade range
            if grade < 0 or grade > 100:
                print(" Grade must be between 0 and 100. Please try again.")
                continue
                
            # Return valid grade
            return grade
            
        except ValueError:
            # Handle non-numeric input
            print(" Invalid input! Please enter a numerical grade (e.g., 85.5).")

def process_student_data(num_students, names_list, grades_list):
    """
    Process data entry for all students using a loop
    Args:
        num_students: total number of students to process
        names_list: list to store student names
        grades_list: list to store student grades
    """
    print(f"\n{'='*40}")
    print("ENTERING STUDENT DATA")
    print('='*40)
    
    # Loop through each student
    student_count = 1
    while student_count <= num_students:
        print(f"\n--- Student {student_count} ---")
        
        # Get student name
        name = input(f"Enter name for student {student_count}: ").strip()
        
        # Validate name is not empty
        if not name:
            print(" Student name cannot be empty. Please try again.")
            continue
        
        # Get validated grade
        grade = get_student_grade(student_count)
        
        # Add data to lists
        names_list.append(name)
        grades_list.append(grade)
        
        # Confirm successful entry
        print(f" Successfully added: {name} - Grade: {grade}")
        
        # Move to next student
        student_count += 1

def calculate_grades(grades_list):
    """
    Calculate total and average grades for the class
    Args: grades_list - list of student grades
    Returns: tuple of (total_grade, average_grade)
    """
    # Calculate total using sum function
    total_grade = sum(grades_list)
    
    # Calculate average (handle division by zero)
    if len(grades_list) > 0:
        average_grade = total_grade / len(grades_list)
    else:
        average_grade = 0
    
    return total_grade, average_grade

def display_results(names, grades, total, average, num_students):
    """
    Display comprehensive results including all student data and statistics
    Args:
        names: list of student names
        grades: list of student grades
        total: total of all grades
        average: average grade
        num_students: number of students
    """
    print(f"\n{'='*50}")
    print("           GRADE REPORT")
    print('='*50)
    
    # Display individual student records
    print("\nINDIVIDUAL STUDENT GRADES:")
    print("-" * 30)
    
    # Loop through each student and display their data
    for i in range(len(names)):
        print(f" {names[i]}: {grades[i]:.2f}")
    
    # Display class statistics
    print(f"\nCLASS STATISTICS:")
    print("-" * 20)
    print(f"Total Students: {num_students}")
    print(f"Total Grade Points: {total:.2f}")
    print(f"Class Average: {average:.2f}")
    
    # Additional analysis
    if grades:  # Only calculate if there are grades
        highest_grade = max(grades)
        lowest_grade = min(grades)
        highest_index = grades.index(highest_grade)
        lowest_index = grades.index(lowest_grade)
        
        print(f"\nPERFORMANCE ANALYSIS:")
        print("-" * 20)
        print(f"Highest Grade: {highest_grade:.2f} ({names[highest_index]})")
        print(f"Lowest Grade: {lowest_grade:.2f} ({names[lowest_index]})")
        print(f"Grade Range: {lowest_grade:.2f} - {highest_grade:.2f}")
    
    print(f"\n{'='*50}")
    print("Thank you for using the Grading System!")
    print('='*50)

# Run the program
if __name__ == "__main__":
    main()