# subjects that will be graded for each student
subjects = ["Mathematics", "English", "Science"]  # List of subject names

# Dictionary to store student records with grades as lists
student_records = {}


# ==================== UTILITY FUNCTIONS ====================

def validate_grade_input(grade_input):
    """Validate and convert grade input to float, return (success, grade)"""
    try:
        grade = float(grade_input)
        if 0 <= grade <= 100:
            return True, grade
        else:
            return False, "Grade must be between 0 and 100"
    except ValueError:
        return False, "Invalid input! Please enter a number"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"


def calculate_average(grades_list):
    """Calculate average of a list of grades"""
    try:
        if not grades_list:
            return 0.0

        # Ensure all grades are numeric
        if not all(isinstance(grade, (int, float)) for grade in grades_list):
            raise ValueError("Non-numeric value found in grades list")

        return sum(grades_list) / len(grades_list)
    except ZeroDivisionError:
        return 0.0
    except Exception as e:
        print(f"Error calculating average: {str(e)}")
        return 0.0


def get_student_grades(student_name):
    """Get grades dictionary for a student, return None if not found"""
    try:
        return student_records.get(student_name)
    except Exception as e:
        print(f"Error retrieving student grades: {str(e)}")
        return None


def get_all_student_names():
    """Return list of all student names"""
    try:
        return list(student_records.keys())
    except Exception as e:
        print(f"Error retrieving student names: {str(e)}")
        return []


def get_total_grades_count():
    """Return total number of grades in system"""
    try:
        total = 0
        for grades_dict in student_records.values():
            if not isinstance(grades_dict, dict):
                continue
            for grades in grades_dict.values():
                if isinstance(grades, list):
                    total += len(grades)
        return total
    except Exception as e:
        print(f"Error counting total grades: {str(e)}")
        return 0


def find_student_matches(search_name):
    """Find exact and partial matches for student name"""
    try:
        if not isinstance(search_name, str):
            return [], []

        exact_matches = []
        partial_matches = []

        for student_name in student_records.keys():
            if not isinstance(student_name, str):
                continue

            if student_name.lower() == search_name.lower():
                exact_matches.append(student_name)
            elif search_name.lower() in student_name.lower():
                partial_matches.append(student_name)

        return exact_matches, partial_matches
    except Exception as e:
        print(f"Error searching for students: {str(e)}")
        return [], []


def select_student_from_matches(matches, prompt):
    """Let user select a student from multiple matches"""
    try:
        if not matches:
            return None

        print(f"\nFound {len(matches)} match(es):")
        for i, name in enumerate(matches, 1):
            print(f"  {i}. {name}")

        choice = input(prompt)
        if not choice.strip():
            print("No selection made!")
            return None

        choice_num = int(choice)
        if 1 <= choice_num <= len(matches):
            return matches[choice_num - 1]
        else:
            print("Invalid selection!")
            return None
    except ValueError:
        print("Invalid input! Please enter a number.")
        return None
    except Exception as e:
        print(f"Error selecting student: {str(e)}")
        return None


# ==================== GRADE ANALYSIS FUNCTIONS ====================

def analyze_subject_performance(grades_list):
    """Analyze performance trends for a subject"""
    try:
        if not isinstance(grades_list, list) or len(grades_list) <= 1:
            return "Insufficient data", 0

        # Validate all grades are numeric
        if not all(isinstance(grade, (int, float)) for grade in grades_list):
            return "Data error", 0

        improvement = grades_list[-1] - grades_list[0]
        if improvement > 0:
            trend = "Improving"
        elif improvement < 0:
            trend = "Declining"
        else:
            trend = "Stable"
        return trend, improvement
    except Exception as e:
        print(f"Error analyzing subject performance: {str(e)}")
        return "Analysis error", 0


def get_performance_category(average):
    """Get performance category based on average grade"""
    try:
        if not isinstance(average, (int, float)):
            return "Invalid data"

        if average >= 90:
            return "Excellent"
        elif average >= 80:
            return "Very Good"
        elif average >= 70:
            return "Good"
        elif average >= 60:
            return "Needs Improvement"
        else:
            return "Poor"
    except Exception as e:
        print(f"Error determining performance category: {str(e)}")
        return "Unknown"


def analyze_grade_distribution(all_grades):
    """Analyze distribution of grades across categories"""
    try:
        if not isinstance(all_grades, list):
            return {
                "A (90-100)": 0, "B (80-89)": 0, "C (70-79)": 0,
                "D (60-69)": 0, "F (0-59)": 0
            }

        distribution = {
            "A (90-100)": len([g for g in all_grades if isinstance(g, (int, float)) and g >= 90]),
            "B (80-89)": len([g for g in all_grades if isinstance(g, (int, float)) and 80 <= g < 90]),
            "C (70-79)": len([g for g in all_grades if isinstance(g, (int, float)) and 70 <= g < 80]),
            "D (60-69)": len([g for g in all_grades if isinstance(g, (int, float)) and 60 <= g < 70]),
            "F (0-59)": len([g for g in all_grades if isinstance(g, (int, float)) and g < 60])
        }
        return distribution
    except Exception as e:
        print(f"Error analyzing grade distribution: {str(e)}")
        return {
            "A (90-100)": 0, "B (80-89)": 0, "C (70-79)": 0,
            "D (60-69)": 0, "F (0-59)": 0
        }


# ==================== DISPLAY FUNCTIONS ====================

def display_header(title):
    """Display a formatted header"""
    try:
        print(f"\n" + "=" * 60)
        print(f" {title}")
        print("=" * 60)
    except Exception as e:
        print(f"\nError displaying header: {str(e)}")


def display_subheader(title):
    """Display a formatted subheader"""
    try:
        if not isinstance(title, str):
            title = str(title)
        print(f"\n{title}:")
        print("-" * len(title))
    except Exception as e:
        print(f"Error displaying subheader: {str(e)}")


def display_student_list():
    """Display list of all students"""
    try:
        if not student_records:
            print("No students in the system!")
            return

        print("\nCurrent students:")
        student_names = get_all_student_names()
        for i, name in enumerate(student_names, 1):
            print(f"  {i}. {name}")
    except Exception as e:
        print(f"Error displaying student list: {str(e)}")


def display_grade_categories(distribution, total_grades):
    """Display grade distribution categories"""
    try:
        if not isinstance(distribution, dict) or not isinstance(total_grades, (int, float)):
            print("  Invalid data for grade distribution")
            return

        for category, count in distribution.items():
            if total_grades > 0:
                percentage = (count / total_grades) * 100
            else:
                percentage = 0
            print(f"  {category}: {count} grades ({percentage:.1f}%)")
    except Exception as e:
        print(f"Error displaying grade categories: {str(e)}")


# ==================== CORE STUDENT OPERATIONS ====================

def get_student_name(prompt, allow_existing=False, require_existing=False):
    """Get and validate student name input"""
    try:
        while True:
            name = input(prompt).strip()
            if not name:
                print("Student name cannot be empty!")
                continue

            if require_existing and name not in student_records:
                print(f"Student '{name}' not found!")
                choice = input("Do you want to try a different name? (y/n): ").lower()
                if choice != 'y':
                    return None
                continue

            if not allow_existing and name in student_records:
                print(f"'{name}' already exists in our database!")
                choice = input("Do you want to enter a different name? (y/n): ").lower()
                if choice != 'y':
                    return None
                continue

            return name
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return None
    except Exception as e:
        print(f"Error getting student name: {str(e)}")
        return None


def input_grades_for_subject(subject):
    """Input multiple grades for a single subject"""
    try:
        if not isinstance(subject, str):
            subject = str(subject)

        grades_list = []
        print(f"\n  {subject} grades:")

        while True:
            try:
                grade_input = input(f"    Enter a grade (0-100) or 'done' to finish: ").strip().lower()

                if grade_input == 'done':
                    if not grades_list:
                        use_default = input("    No grades entered. Use 0 as default? (y/n): ").lower()
                        if use_default == 'y':
                            grades_list = [0.0]
                    break

                success, result = validate_grade_input(grade_input)
                if success:
                    grades_list.append(result)
                    print(f"    ✓ Added grade: {result}. Current {subject} grades: {grades_list}")

                    if len(grades_list) >= 1:
                        more_grades = input("    Add another grade? (y/n): ").lower()
                        if more_grades != 'y':
                            break
                else:
                    print(f"    Error: {result}")
            except KeyboardInterrupt:
                print("\n    Grade input cancelled.")
                break
            except Exception as e:
                print(f"    Unexpected error: {str(e)}")
                continue

        return grades_list
    except Exception as e:
        print(f"Error inputting grades for subject: {str(e)}")
        return []


def manage_subject_grades(student_name, subject):
    """Manage grades for a specific subject (add/remove/clear)"""
    try:
        if student_name not in student_records:
            print(f"Student '{student_name}' not found!")
            return

        current_grades = student_records[student_name].get(subject, [])
        print(f"    Current {subject} grades: {current_grades}")

        while True:
            try:
                action = input("    Choose action - (a)dd new grade, (r)emove grade, (c)lear all, (s)kip: ").lower()

                if action == 's':  # Skip this subject
                    break
                elif action == 'a':  # Add new grade
                    grade_input = input("    Enter new grade (0-100): ")
                    success, result = validate_grade_input(grade_input)
                    if success:
                        current_grades.append(result)
                        student_records[student_name][subject] = current_grades
                        print(f"    ✓ Added new grade. Current {subject} grades: {current_grades}")
                    else:
                        print(f"    Error: {result}")

                elif action == 'r':  # Remove a grade
                    if not current_grades:
                        print("    No grades to remove!")
                        continue

                    print(f"    Current grades: {current_grades}")
                    try:
                        index_input = input("    Enter index of grade to remove (0 for first grade): ")
                        if not index_input.strip():
                            print("    No index provided!")
                            continue

                        index = int(index_input)
                        if 0 <= index < len(current_grades):
                            removed_grade = current_grades.pop(index)
                            student_records[student_name][subject] = current_grades
                            print(f"    ✓ Removed grade {removed_grade}. Current grades: {current_grades}")
                        else:
                            print("    Invalid index!")
                    except ValueError:
                        print("    Please enter a valid number!")
                    except Exception as e:
                        print(f"    Error removing grade: {str(e)}")

                elif action == 'c':  # Clear all grades
                    confirm = input("    Are you sure you want to clear all grades for this subject? (y/n): ").lower()
                    if confirm == 'y':
                        student_records[student_name][subject] = []
                        current_grades = []
                        print(f"    ✓ Cleared all {subject} grades.")
                    break
                else:
                    print("    Invalid action! Please choose a, r, c, or s.")
            except KeyboardInterrupt:
                print("\n    Operation cancelled.")
                break
            except Exception as e:
                print(f"    Error in grade management: {str(e)}")
                continue
    except Exception as e:
        print(f"Error managing subject grades: {str(e)}")


# ==================== SEARCH AND UPDATE FUNCTIONS ====================

def search_and_select_student(purpose="view"):
    """Search for a student and return selected name, or None if not found/cancelled"""
    try:
        if not student_records:
            print("No students in the system!")
            return None

        display_header(f"SEARCH STUDENT TO {purpose.upper()}")

        search_name = input("Enter student name to search for: ").strip()
        if not search_name:
            print("Search term cannot be empty!")
            return None

        exact_matches, partial_matches = find_student_matches(search_name)

        # Handle search results
        if exact_matches:
            if len(exact_matches) == 1:
                return exact_matches[0]
            else:
                return select_student_from_matches(exact_matches,
                                                   f"\nSelect student to {purpose} (1-{len(exact_matches)}): ")

        elif partial_matches:
            if len(partial_matches) == 1:
                choice = input(f"\nFound '{partial_matches[0]}'. Select this student? (y/n): ").lower()
                if choice == 'y':
                    return partial_matches[0]
                else:
                    return None
            else:
                return select_student_from_matches(partial_matches,
                                                   f"\nSelect student to {purpose} (1-{len(partial_matches)} or 0 to cancel): ")

        else:
            print(f"\n No students found matching '{search_name}'")
            available_students = get_all_student_names()
            if available_students:
                print("Available students:", available_students)
            return None
    except KeyboardInterrupt:
        print("\nSearch cancelled by user.")
        return None
    except Exception as e:
        print(f"Error during student search: {str(e)}")
        return None


def search_and_update_grades():
    """Search for a student and update their grades in one workflow"""
    try:
        student_name = search_and_select_student("update")

        if student_name is None:
            return

        print(f"\nUpdating grades for {student_name}:")
        print("Current grades:")
        for subject, grades in student_records[student_name].items():
            print(f"  {subject}: {grades}")

        update_count = 0
        for subject in subjects:
            try:
                print(f"\n  Updating {subject} grades:")
                current_grades = student_records[student_name].get(subject, [])

                while True:
                    try:
                        action = input(
                            "    Choose action - (a)dd new grade, (r)emove grade, (c)lear all, (s)kip: ").lower()

                        if action == 's':  # Skip this subject
                            break
                        elif action == 'a':  # Add new grade
                            grade_input = input("    Enter new grade (0-100): ")
                            success, result = validate_grade_input(grade_input)
                            if success:
                                current_grades.append(result)
                                student_records[student_name][subject] = current_grades
                                update_count += 1
                                print(f"    ✓ Added new grade. Current {subject} grades: {current_grades}")
                            else:
                                print(f"    Error: {result}")

                        elif action == 'r':  # Remove a grade
                            if not current_grades:
                                print("    No grades to remove!")
                                continue

                            print(f"    Current grades: {current_grades}")
                            try:
                                index_input = input("    Enter index of grade to remove (0 for first grade): ")
                                if not index_input.strip():
                                    print("    No index provided!")
                                    continue

                                index = int(index_input)
                                if 0 <= index < len(current_grades):
                                    removed_grade = current_grades.pop(index)
                                    student_records[student_name][subject] = current_grades
                                    update_count += 1
                                    print(f"    ✓ Removed grade {removed_grade}. Current grades: {current_grades}")
                                else:
                                    print("    Invalid index!")
                            except ValueError:
                                print("    Please enter a valid number!")

                        elif action == 'c':  # Clear all grades
                            confirm = input(
                                "    Are you sure you want to clear all grades for this subject? (y/n): ").lower()
                            if confirm == 'y':
                                student_records[student_name][subject] = []
                                current_grades = []
                                update_count += 1
                                print(f"    ✓ Cleared all {subject} grades.")
                            break
                        else:
                            print("    Invalid action! Please choose a, r, c, or s.")

                    except KeyboardInterrupt:
                        print("\n    Operation cancelled.")
                        break
                    except Exception as e:
                        print(f"    Unexpected error: {str(e)}")
                        continue

            except Exception as e:
                print(f"    Error updating {subject}: {str(e)}")
                continue

        if update_count > 0:
            print(f"\n Successfully updated {update_count} item(s) for {student_name}")
            print("Final grades:")
            for subject, grades in student_records[student_name].items():
                print(f"  {subject}: {grades}")
        else:
            print(f"\n  No changes made to {student_name}'s grades")
    except Exception as e:
        print(f"Error in search and update grades: {str(e)}")


# ==================== MAIN FEATURE FUNCTIONS ====================

def add_student():
    """Add a new student to the system with multiple grades per subject"""
    try:
        student_name = get_student_name("\nEnter student name: ")
        if student_name is None:
            return

        student_grades = {}
        print(f"Entering grades for {student_name}:")

        for subject in subjects:
            try:
                grades_list = input_grades_for_subject(subject)
                student_grades[subject] = grades_list
            except Exception as e:
                print(f"Error processing {subject}: {str(e)}")
                student_grades[subject] = []

        student_records[student_name] = student_grades
        print(f"\n Added {student_name} with grades:")
        for subject, grades in student_grades.items():
            print(f"  {subject}: {grades}")
    except Exception as e:
        print(f"Error adding student: {str(e)}")


def update_grades():
    """Update grades for an existing student (exact name required)"""
    try:
        if not student_records:
            print(" No students in the system!")
            return

        display_student_list()
        student_name = get_student_name("Enter student name to update: ", require_existing=True)

        if student_name is None:
            return

        print(f"\nUpdating grades for {student_name}:")
        print("Current grades:")
        for subject, grades in student_records[student_name].items():
            print(f"  {subject}: {grades}")

        update_count = 0
        for subject in subjects:
            try:
                print(f"\n  Updating {subject} grades:")
                manage_subject_grades(student_name, subject)
            except Exception as e:
                print(f"    Error updating {subject}: {str(e)}")
                continue

        print(f"\n Updated {student_name}'s grades:")
        for subject, grades in student_records[student_name].items():
            print(f"  {subject}: {grades}")
    except Exception as e:
        print(f"Error updating grades: {str(e)}")


def remove_student():
    """Remove a student from the system"""
    try:
        student_name = search_and_select_student("remove")

        if student_name is None:
            return

        # Show student details before removal
        print(f"\nStudent to remove: {student_name}")
        display_student_details(student_name)

        confirm = input(f"\n  Are you sure you want to remove {student_name}? (y/n): ").lower()
        if confirm == 'y':
            del student_records[student_name]
            print(f" Removed student '{student_name}' from the system")
        else:
            print("ℹ  Removal cancelled.")
    except KeyError:
        print(f"Student '{student_name}' not found in records!")
    except Exception as e:
        print(f"Error removing student: {str(e)}")


def search_student():
    """Search for a specific student by name and display their grades and averages"""
    try:
        student_name = search_and_select_student("view details")

        if student_name is not None:
            display_student_details(student_name)
    except Exception as e:
        print(f"Error searching for student: {str(e)}")


def display_student_details(student_name):
    """Display detailed grade information for a specific student"""
    try:
        display_header(f"STUDENT REPORT: {student_name.upper()}")

        grades_dict = get_student_grades(student_name)
        if not grades_dict:
            print(" No grade data available for this student.")
            return

        subject_averages = {}
        all_grades = []

        display_subheader("GRADE BREAKDOWN")

        for subject in subjects:
            try:
                grades_list = grades_dict.get(subject, [])
                if grades_list:
                    subject_avg = calculate_average(grades_list)
                    subject_averages[subject] = subject_avg
                    all_grades.extend(grades_list)

                    print(f"\n{subject}:")
                    print(f"  Grades: {grades_list}")
                    print(f"  Average: {subject_avg:.2f}")
                    print(f"  Number of assessments: {len(grades_list)}")

                    # Grade analysis for the subject
                    trend, improvement = analyze_subject_performance(grades_list)
                    if trend != "Insufficient data":
                        print(f"  Trend: {trend} ({improvement:+.1f} points)")
                else:
                    print(f"\n{subject}: No grades available")
                    subject_averages[subject] = 0.0
            except Exception as e:
                print(f"  Error processing {subject}: {str(e)}")
                continue

        # Display overall statistics
        if all_grades:
            try:
                overall_avg = calculate_average(all_grades)
                if subject_averages:
                    highest_subject = max(subject_averages.items(), key=lambda x: x[1])
                    lowest_subject = min(subject_averages.items(), key=lambda x: x[1])
                else:
                    highest_subject = ("None", 0)
                    lowest_subject = ("None", 0)

                display_subheader("OVERALL PERFORMANCE")
                print(f"Overall Average: {overall_avg:.2f}")
                print(f"Total Assessments: {len(all_grades)}")
                print(f"Strongest Subject: {highest_subject[0]} ({highest_subject[1]:.2f})")
                print(f"Subject Needing Improvement: {lowest_subject[0]} ({lowest_subject[1]:.2f})")

                performance = get_performance_category(overall_avg)
                print(f"Performance: {performance}")

                # Display grade distribution
                display_subheader("GRADE DISTRIBUTION")
                distribution = analyze_grade_distribution(all_grades)
                display_grade_categories(distribution, len(all_grades))
            except Exception as e:
                print(f"Error calculating overall statistics: {str(e)}")
        else:
            print(f"\n No grades available for {student_name}")
    except Exception as e:
        print(f"Error displaying student details: {str(e)}")


def display_all_students():
    """Display all students and their grades"""
    try:
        if not student_records:
            print(" No students in the system!")
            return

        display_header("ALL STUDENT RECORDS")
        print(f"Total Students: {len(student_records)}")

        for student_name, grades_dict in student_records.items():
            try:
                # Calculate overall average
                all_grades = []
                for subject_grades in grades_dict.values():
                    if isinstance(subject_grades, list):
                        all_grades.extend(subject_grades)

                overall_average = calculate_average(all_grades)

                print(f"\nStudent: {student_name}")
                for subject, grades_list in grades_dict.items():
                    if grades_list and isinstance(grades_list, list):
                        subject_avg = calculate_average(grades_list)
                        print(f"  {subject}: {grades_list} (Avg: {subject_avg:.2f})")
                    else:
                        print(f"  {subject}: No grades")
                print(f"  Overall Average: {overall_average:.2f}")
                print("-" * 50)
            except Exception as e:
                print(f"Error processing student {student_name}: {str(e)}")
                continue
    except Exception as e:
        print(f"Error displaying all students: {str(e)}")


def view_subject_grades():
    """View grades for a specific subject across all students"""
    try:
        if not student_records:
            print(" No students in the system!")
            return

        print("\nAvailable subjects:", subjects)
        subject = input("Enter subject name to view grades: ").strip()

        if subject not in subjects:
            print(f" Subject '{subject}' not found in available subjects!")
            return

        display_header(f"GRADES FOR {subject.upper()} - ALL STUDENTS")

        subject_grades_summary = []

        for student_name, grades_dict in student_records.items():
            try:
                grades_list = grades_dict.get(subject, [])
                if grades_list and isinstance(grades_list, list):
                    student_avg = calculate_average(grades_list)
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
            except Exception as e:
                print(f"Error processing {student_name}: {str(e)}")
                continue

        # Display subject statistics
        if subject_grades_summary:
            try:
                all_grades = []
                for entry in subject_grades_summary:
                    if isinstance(entry.get('grades'), list):
                        all_grades.extend(entry['grades'])

                if all_grades:
                    subject_highest = max(all_grades)
                    subject_lowest = min(all_grades)
                    subject_average = calculate_average(all_grades)

                    display_subheader(f"{subject.upper()} CLASS STATISTICS")
                    print(f"  Highest grade: {subject_highest:.2f}")
                    print(f"  Lowest grade: {subject_lowest:.2f}")
                    print(f"  Class average: {subject_average:.2f}")
                    print(f"  Total assessments: {len(all_grades)}")
                    print(f"  Students with grades: {len(subject_grades_summary)}")
            except Exception as e:
                print(f"Error calculating subject statistics: {str(e)}")
    except Exception as e:
        print(f"Error viewing subject grades: {str(e)}")


def calculate_statistics():
    """Calculate and display average grades and subject analysis"""
    try:
        if not student_records:
            print(" No students in the system!")
            return

        # Individual student averages
        display_header("STUDENT OVERALL AVERAGES")

        for student_name, grades_dict in student_records.items():
            try:
                all_grades = []
                for subject_grades in grades_dict.values():
                    if isinstance(subject_grades, list):
                        all_grades.extend(subject_grades)

                if all_grades:
                    overall_average = calculate_average(all_grades)
                    print(f"{student_name}: Overall Average = {overall_average:.2f} (from {len(all_grades)} grades)")
                else:
                    print(f"{student_name}: No grades available")
            except Exception as e:
                print(f"Error processing {student_name}: {str(e)}")
                continue

        # Subject analysis
        display_header("SUBJECT ANALYSIS")

        for subject in subjects:
            try:
                all_subject_grades = []
                student_count_with_grades = 0

                for grades_dict in student_records.values():
                    subject_grades = grades_dict.get(subject, [])
                    if subject_grades and isinstance(subject_grades, list):
                        all_subject_grades.extend(subject_grades)
                        student_count_with_grades += 1

                if all_subject_grades:
                    highest_grade = max(all_subject_grades)
                    lowest_grade = min(all_subject_grades)
                    subject_average = calculate_average(all_subject_grades)

                    print(f"\n{subject}:")
                    print(f"  Highest grade: {highest_grade:.2f}")
                    print(f"  Lowest grade: {lowest_grade:.2f}")
                    print(f"  Subject average: {subject_average:.2f}")
                    print(f"  Total assessments: {len(all_subject_grades)}")
                    print(f"  Students with grades: {student_count_with_grades}/{len(student_records)}")
                else:
                    print(f"\n{subject}: No grades available")
            except Exception as e:
                print(f"Error analyzing {subject}: {str(e)}")
                continue
    except Exception as e:
        print(f"Error calculating statistics: {str(e)}")


def display_student_count():
    """Display current number of students"""
    try:
        count = len(student_records)
        total_grades = get_total_grades_count()

        print(f"\nCurrent number of students in system: {count}")
        if count > 0:
            student_names = get_all_student_names()
            if student_names:
                print("Students:", ", ".join(student_names))

                # Show grade statistics
                for student_name in student_names:
                    try:
                        grades_dict = student_records.get(student_name, {})
                        student_grades_count = 0
                        for grades in grades_dict.values():
                            if isinstance(grades, list):
                                student_grades_count += len(grades)
                        print(f"  {student_name}: {student_grades_count} grades")
                    except Exception as e:
                        print(f"  Error processing {student_name}: {str(e)}")
                        continue

                print(f"\nTotal grades in system: {total_grades}")
        else:
            print("The system is empty.")
    except Exception as e:
        print(f"Error displaying student count: {str(e)}")


# ==================== MENU AND MAIN PROGRAM ====================

def display_menu():
    """Display the main menu"""
    try:
        student_count = len(student_records)
        total_grades = get_total_grades_count()

        display_header("STUDENT GRADE MANAGEMENT SYSTEM")
        print(f"Students: {student_count} | Total Grades: {total_grades}")
        print("=" * 60)
        print("1. Add new student (with multiple grades per subject)")
        print("2. Update student grades (exact name required)")
        print("3. Search and update grades (partial name search)")
        print("4. Remove student")
        print("5. Display all students")
        print("6. Search for student and view their report")
        print("7. View grades for specific subject")
        print("8. Calculate statistics")
        print("9. Show student count and summary")
        print("10. Exit")
        print("=" * 60)
    except Exception as e:
        print(f"Error displaying menu: {str(e)}")


def main():
    """Main program loop"""
    try:
        print("GABORONE CITY UNIVERSITY SYSTEM")

        # Main menu loop
        while True:
            try:
                display_menu()
                choice = input("\nEnter your choice (1-10): ").strip()

                if choice == '1':
                    add_student()
                elif choice == '2':
                    update_grades()
                elif choice == '3':
                    search_and_update_grades()
                elif choice == '4':
                    remove_student()
                elif choice == '5':
                    display_all_students()
                elif choice == '6':
                    search_student()
                elif choice == '7':
                    view_subject_grades()
                elif choice == '8':
                    calculate_statistics()
                elif choice == '9':
                    display_student_count()
                elif choice == '10':
                    print("\nThank you for using the Student Grade Management System!")
                    print(f"Final student count: {len(student_records)}")
                    break
                else:
                    print(" Invalid choice! Please enter a number between 1-10.")

                # Small pause to let user read the output
                input("\nPress Enter to continue...")

            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user. Returning to main menu...")
            except Exception as e:
                print(f"\nUnexpected error in menu operation: {str(e)}")
                print("Returning to main menu...")

    except KeyboardInterrupt:
        print("\n\nProgram terminated by user. Goodbye!")
    except Exception as e:
        print(f"Fatal error in main program: {str(e)}")
        print("Program terminated.")


# Run the program
if __name__ == "__main__":
    main()