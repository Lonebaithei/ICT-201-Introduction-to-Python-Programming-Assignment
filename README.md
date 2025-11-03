# ICT 201 Introduction to Python Programming 
ICT 201 Introduction to Python Programming Assignment 

Project Overview:
-----

#  Student Grade Management System

A comprehensive Python-based system for managing student grades. It features robust exception handling, advanced searching and sorting, and detailed performance analysis.

##  Features

  *  Exception Handling: Utilizes custom exceptions (e.g., `StudentNotFoundError`, `InvalidGradeError`) for clean error recovery and user-friendly messaging.
  *  Data Management: Classes for `Student` and `Gradebook` to handle grades, subject averages, and overall performance.
  * Searching & Sorting:
      * Advanced Search: Supports searching by name (exact, similar matches), performance category, and grade range.
      * Sorting: Includes efficient sorting by name (optimized **Bubble Sort**) and overall/subject average.
  * Performance Analysis: Provides subject statistics (high/low/average), class averages, top performers, and overall grade distribution.
  * Comprehensive Testing: Includes a built-in test suite for custom exceptions, sorting algorithms, and grade validation.

## To Get Started

### Prerequisites

  * Python 3.x

### Running the Application

1.  Save the provided code as `Baithei_Lone_SectionE+F.py`.

2.  Run the application from your terminal:

    ```bash
    python Baithei_Lone_SectionE+F.py
    ```

### Optional Commands

The system also supports direct running of the demo or test suite:

  * Run Demo:
    ```bash
    python Baithei_Lone_SectionE+F.py demo
    ```
  * Run Tests:
    ```bash
    python Baithei_Lone_SectionE+F.py test
    ```

## 🛠 Project Structure

The project is logically divided into three main components:

1.  Custom Exceptions: Handles specific application errors (e.g., `StudentNotFoundError`).
2.  `Student` Class: Represents an individual student and manages their grades and personal performance analysis.
3.  `Gradebook` Class: Manages a collection of students, providing searching, sorting, and class-level statistical operations.
4.  `GradeManager` Class: The main application interface, handling user interaction, menu display, and error recovery.
