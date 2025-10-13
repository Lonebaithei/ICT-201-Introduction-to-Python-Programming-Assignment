# subjects that will be graded for each student
subjects = ["Mathematics", "English", "Science"]  # List of subject names

# Dictionary to store student records with grades as lists
student_records = {}

def search_student():
    """Search student by name and display their grades and averages"""
    if not student_records:
        print("No students in the system!")
        return

    print("\n" + "=" * 50)
    print("SEARCH STUDENT")
    print("=" * 50)
    
    search_name = input("Enter student name to search for: ").strip()
    
    # Search for exact and partial matches
    exact_matches = []
    partial_matches = []
    
    for student_name in student_records.keys():
        if student_name.lower() == search_name.lower():
            exact_matches.append(student_name)
        elif search_name.lower() in student_name.lower():
            partial_matches.append(student_name)
    
    # Handle search results
    if exact_matches:
        display_student_details(exact_matches[0])
    elif partial_matches:
        print(f"\nFound {len(partial_matches)} partial match(es):")
        for i, name in enumerate(partial_matches, 1):
            print(f"  {i}. {name}")
        
        if len(partial_matches) == 1:
            choice = input("\nSelect this student? (y/n): ").lower()
            if choice == 'y':
                display_student_details(partial_matches[0])
        else:
            try:
                choice = int(input("\nEnter the number of the student to view details (or 0 to cancel): "))
                if 1 <= choice <= len(partial_matches):
                    display_student_details(partial_matches[choice - 1])
            except ValueError:
                print("Invalid input! Please enter a number.")
    else:
        print(f"\n No students found matching '{search_name}'")
        print("Available students:", list(student_records.keys()))

def display_student_details(student_name):
    """Display students grades information"""
    print(f"\n" + "=" * 60)
    print(f" STUDENT REPORT: {student_name.upper()}")
    print("=" * 60)
    
    grades_dict = student_records[student_name]
    
    # Calculate subject averages and overall average
    subject_averages = {}
    all_grades = []
    
    print(f"\n📝 GRADE BREAKDOWN:")
    print("-" * 50)
    
    for subject in subjects:
        grades_list = grades_dict.get(subject, [])
        if grades_list:
            subject_avg = sum(grades_list) / len(grades_list)
            subject_averages[subject] = subject_avg
            all_grades.extend(grades_list)
            
            print(f"\n{subject}:")
            print(f"  Grades: {grades_list}")
            print(f"  Average: {subject_avg:.2f}")
            print(f"  Number of assessments: {len(grades_list)}")
            
            # Grade analysis for the subject
            if len(grades_list) > 1:
                improvement = grades_list[-1] - grades_list[0]
                trend = " Improving" if improvement > 0 else " Declining" if improvement < 0 else " Stable"
                print(f"  Trend: {trend} ({improvement:+.1f} points)")
        else:
            print(f"\n{subject}: No grades available")
            subject_averages[subject] = 0.0
    
    # Display overall statistics
    if all_grades:
        overall_avg = sum(all_grades) / len(all_grades)
        highest_subject = max(subject_averages.items(), key=lambda x: x[1])
        lowest_subject = min(subject_averages.items(), key=lambda x: x[1])
        
        print(f"\n OVERALL PERFORMANCE:")
        print("-" * 30)
        print(f"Overall Average: {overall_avg:.2f}")
        print(f"Total Assessments: {len(all_grades)}")
        print(f"Strongest Subject: {highest_subject[0]} ({highest_subject[1]:.2f})")
        print(f"Subject Needing Improvement: {lowest_subject[0]} ({lowest_subject[1]:.2f})")
        
        # Performance category
        if overall_avg >= 90:
            performance = " Excellent"
        elif overall_avg >= 80:
            performance = " Very Good"
        elif overall_avg >= 70:
            performance = " Good"
        elif overall_avg >= 60:
            performance = "  Needs Improvement"
        else:
            performance = " Poor"
            
        print(f"Performance: {performance}")
        
        # Display grade distribution
        print(f"\n GRADE DISTRIBUTION:")
        grade_categories = {
            "A (90-100)": len([g for g in all_grades if g >= 90]),
            "B (80-89)": len([g for g in all_grades if 80 <= g < 90]),
            "C (70-79)": len([g for g in all_grades if 70 <= g < 80]),
            "D (60-69)": len([g for g in all_grades if 60 <= g < 70]),
            "F (0-59)": len([g for g in all_grades if g < 60])
        }
        
        for category, count in grade_categories.items():
            percentage = (count / len(all_grades)) * 100 if all_grades else 0
            print(f"  {category}: {count} grades ({percentage:.1f}%)")
    
    else:
        print(f"\n No grades available for {student_name}")

def add_student():
    """Add a new student to the system with multiple grades per subject"""
    student_name = input("\nEnter student name: ").strip()

    if student_name in student_records:
        print(f"'{student_name}' already exists in our database!")
        return

    student_grades = {}  # Dictionary for subject:list_of_grades pairs

    print(f"Entering grades for {student_name}:")
    for subject in subjects:
        grades_list = []  # List to store multiple grades for this subject
        print(f"\n  {subject} grades:")
        
        while True:
            try:
                grade_input = input(f"    Enter a grade (0-100) or 'done' to finish: ").strip().lower()
                
                if grade_input == 'done':
                    if not grades_list:  # If no grades entered, add a default 0
                        use_default = input("    No grades entered. Use 0 as default? (y/n): ").lower()
                        if use_default == 'y':
                            grades_list = [0.0]
                    break
                
                grade = float(grade_input)

                if grade < 0 or grade < 0 or grade > 100:
                    print("    Error: Grade must be between 0 and 100. Please try again.")
                    continue

                grades_list.append(grade)
                print(f"    ✓ Added grade: {grade}. Current {subject} grades: {grades_list}")
                
                # Ask if user wants to add more grades
                if len(grades_list) >= 1:
                    more_grades = input("    Add another grade? (y/n): ").lower()
                    if more_grades != 'y':
                        break

            except ValueError:
                print("    Invalid input! Please enter a number between 0-100 or 'done' to finish")

        student_grades[subject] = grades_list

    student_records[student_name] = student_grades
    print(f"\n✓ Added {student_name} with grades:")
    for subject, grades in student_grades.items():
        print(f"  {subject}: {grades}")

def update_grades():
    """Update grades for an existing student - now handles lists of grades"""
    if not student_records:
        print("No students in the system!")
        return

    print("\nCurrent students:", list(student_records.keys()))
    student_name = input("Enter student name to update: ").strip()

    if student_name not in student_records:
        print(f"Student '{student_name}' not found!")
        return

    print(f"\nUpdating grades for {student_name}:")
    print("Current grades:")
    for subject, grades in student_records[student_name].items():
        print(f"  {subject}: {grades}")

    for subject in subjects:
        print(f"\n  Updating {subject} grades:")
        current_grades = student_records[student_name].get(subject, [])
        print(f"    Current {subject} grades: {current_grades}")
        
        while True:
            try:
                action = input("    Choose action - (a)dd new grade, (r)emove grade, (c)lear all, (s)kip: ").lower()
                
                if action == 's':  # Skip this subject
                    break
                elif action == 'a':  # Add new grade
                    grade_input = input("    Enter new grade (0-100): ")
                    new_grade = float(grade_input)
                    
                    if new_grade < 0 or new_grade > 100:
                        print("    Error: Grade must be between 0 and 100.")
                        continue
                    
                    current_grades.append(new_grade)
                    student_records[student_name][subject] = current_grades
                    print(f"    ✓ Added new grade. Current {subject} grades: {current_grades}")
                    
                elif action == 'r':  # Remove a grade
                    if not current_grades:
                        print("    No grades to remove!")
                        continue
                    
                    print(f"    Current grades: {current_grades}")
                    try:
                        index = int(input("    Enter index of grade to remove (0 for first grade): "))
                        if 0 <= index < len(current_grades):
                            removed_grade = current_grades.pop(index)
                            student_records[student_name][subject] = current_grades
                            print(f"    ✓ Removed grade {removed_grade}. Current grades: {current_grades}")
                        else:
                            print("    Invalid index!")
                    except ValueError:
                        print("    Please enter a valid number!")
                        
                elif action == 'c':  # Clear all grades
                    confirm = input("    Are you sure you want to clear all grades for this subject? (y/n): ").lower()
                    if confirm == 'y':
                        student_records[student_name][subject] = []
                        current_grades = []
                        print(f"    ✓ Cleared all {subject} grades.")
                    break
                else:
                    print("    Invalid action! Please choose a, r, c, or s.")
                    
            except ValueError:
                print("    Invalid input! Please enter a valid number.")

    print(f"\n✓ Updated {student_name}'s grades:")
    for subject, grades in student_records[student_name].items():
        print(f"  {subject}: {grades}")

def remove_student():
    """Remove a student from the system"""
    if not student_records:
        print("No students in the system!")
        return

    print("\nCurrent students:", list(student_records.keys()))
    student_name = input("Enter student name to remove: ").strip()

    if student_name in student_records:
        # Show student details before removal
        print(f"\nStudent to remove: {student_name}")
        display_student_details(student_name)
        
        confirm = input(f"\nAre you sure you want to remove {student_name}? (y/n): ").lower()
        if confirm == 'y':
            del student_records[student_name]
            print(f"✓ Removed student '{student_name}' from the system")
        else:
            print("Removal cancelled.")
    else:
        print(f"Student '{student_name}' not found!")

def display_all_students():
    """Display all students and their grades"""
    if not student_records:
        print("No students in the system!")
        return

    print("\n" + "=" * 60)
    print("ALL STUDENT RECORDS")
    print(f"Total Students: {len(student_records)}")
    print("=" * 60)

    for student_name, grades_dict in student_records.items():
        # Calculate overall average (average of all grades across all subjects)
        all_grades = []
        for subject_grades in grades_dict.values():
            all_grades.extend(subject_grades)
        
        if all_grades:
            overall_average = sum(all_grades) / len(all_grades)
        else:
            overall_average = 0.0
            
        print(f"\nStudent: {student_name}")
        for subject, grades_list in grades_dict.items():
            if grades_list:
                subject_avg = sum(grades_list) / len(grades_list)
                print(f"  {subject}: {grades_list} (Avg: {subject_avg:.2f})")
            else:
                print(f"  {subject}: No grades")
        print(f"  Overall Average: {overall_average:.2f}")
        print("-" * 50)

def view_subject_grades():
    """View grades for a specific subject across all students"""
    if not student_records:
        print("No students in the system!")
        return

    print("\nAvailable subjects:", subjects)
    subject = input("Enter subject name to view grades: ").strip()

    if subject not in subjects:
        print(f"Subject '{subject}' not found in available subjects!")
        return

    print(f"\n" + "=" * 50)
    print(f"GRADES FOR {subject.upper()} - ALL STUDENTS")
    print("=" * 50)

    subject_grades_summary = []
    
    for student_name, grades_dict in student_records.items():
        grades_list = grades_dict.get(subject, [])
        if grades_list:
            student_avg = sum(grades_list) / len(grades_list)
            subject_grades_summary.append({
                'student': student_name,
                'grades': grades_list,
                'average': student_avg
            })
            print(f"{student_name}:")
            print(f"  Grades: {grades_list}")
            print(f"  Average: {student_avg:.2f}")
            print(f"  Number of assessments: {len(grades_list)}")
            print("-" * 30)
        else:
            print(f"{student_name}: No grades available")
            print("-" * 30)

    # Display subject statistics
    if subject_grades_summary:
        all_grades = []
        for entry in subject_grades_summary:
            all_grades.extend(entry['grades'])
        
        if all_grades:
            subject_highest = max(all_grades)
            subject_lowest = min(all_grades)
            subject_average = sum(all_grades) / len(all_grades)
            
            print(f"\n {subject.upper()} CLASS STATISTICS:")
            print(f"  Highest grade: {subject_highest:.2f}")
            print(f"  Lowest grade: {subject_lowest:.2f}")
            print(f"  Class average: {subject_average:.2f}")
            print(f"  Total assessments: {len(all_grades)}")
            print(f"  Students with grades: {len(subject_grades_summary)}")

def calculate_statistics():
    """Calculate and display average grades and subject analysis"""
    if not student_records:
        print("No students in the system!")
        return

    # Individual student averages (overall average across all subjects)
    print("\n" + "=" * 50)
    print("STUDENT OVERALL AVERAGES")
    print("=" * 50)

    for student_name, grades_dict in student_records.items():
        all_grades = []
        for subject_grades in grades_dict.values():
            all_grades.extend(subject_grades)
        
        if all_grades:
            overall_average = sum(all_grades) / len(all_grades)
            print(f"{student_name}: Overall Average = {overall_average:.2f} (from {len(all_grades)} grades)")
        else:
            print(f"{student_name}: No grades available")

    # Subject analysis
    print("\n" + "=" * 50)
    print("SUBJECT ANALYSIS")
    print("=" * 50)

    for subject in subjects:
        all_subject_grades = []
        student_count_with_grades = 0
        
        for grades_dict in student_records.values():
            subject_grades = grades_dict.get(subject, [])
            if subject_grades:
                all_subject_grades.extend(subject_grades)
                student_count_with_grades += 1

        if all_subject_grades:
            highest_grade = max(all_subject_grades)
            lowest_grade = min(all_subject_grades)
            subject_average = sum(all_subject_grades) / len(all_subject_grades)
            
            print(f"\n{subject}:")
            print(f"  Highest grade: {highest_grade:.2f}")
            print(f"  Lowest grade: {lowest_grade:.2f}")
            print(f"  Subject average: {subject_average:.2f}")
            print(f"  Total assessments: {len(all_subject_grades)}")
            print(f"  Students with grades: {student_count_with_grades}/{len(student_records)}")
        else:
            print(f"\n{subject}: No grades available")

def display_student_count():
    """Display current number of students"""
    count = len(student_records)
    print(f"\nCurrent number of students in system: {count}")
    if count > 0:
        print("Students:", ", ".join(student_records.keys()))
        
        # Show grade statistics
        total_grades = 0
        for student_name, grades_dict in student_records.items():
            student_grades_count = sum(len(grades) for grades in grades_dict.values())
            total_grades += student_grades_count
            print(f"  {student_name}: {student_grades_count} grades")
        
        print(f"\nTotal grades in system: {total_grades}")
    else:
        print("The system is empty.")

def display_menu():
    """Display the main menu"""
    student_count = len(student_records)
    
    # Calculate total grades for display
    total_grades = 0
    for grades_dict in student_records.values():
        total_grades += sum(len(grades) for grades in grades_dict.values())
    
    print("\n" + "=" * 60)
    print("STUDENT GRADE MANAGEMENT SYSTEM")
    print(f"Students: {student_count} | Total Grades: {total_grades}")
    print("=" * 60)
    print("1. Add new student (with multiple grades per subject)")
    print("2. Update student grades")
    print("3. Remove student")
    print("4. Display all students")
    print("5. Search for student and view their report")
    print("6. View grades for specific subject")
    print("7. Calculate statistics")
    print("8. Show student count and summary")
    print("9. Exit")
    print("=" * 60)

def main():
    print("GABORONE UNIVERSITY STUDENT GRADE MANAGEMENT SYSTEM")
    
    

    # Main menu loop
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-9): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            update_grades()
        elif choice == '3':
            remove_student()
        elif choice == '4':
            display_all_students()
        elif choice == '5':
            search_student()
        elif choice == '6':
            view_subject_grades()
        elif choice == '7':
            calculate_statistics()
        elif choice == '8':
            display_student_count()
        elif choice == '9':
            print("\nThank you for using the Student Grade Management System!")
            print(f"Final student count: {len(student_records)}")
            break
        else:
            print("Invalid choice! Please enter a number between 1-9.")

# Run the program
if __name__ == "__main__":
    main()