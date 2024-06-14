# Gradesheet-Generator

Gradesheet-Generator is a robust Django application designed to automate the generation and distribution of gradesheets for students in an educational institute. The project features user authentication, OTP verification, and integrates email functionality to ensure secure access to gradesheets.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Models Overview](#models-overview)
- [Admin Interface](#admin-interface)
- [Views and URLs](#views-and-urls)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**: Secure login for students to access their grades.
- **OTP Verification**: OTP sent via email to verify student identity.
- **Gradesheet Generation**: Automated gradesheet generation based on provided student marks.
- **Email Integration**: Sends OTP and notifications to students.
- **Search and Pagination**: Efficient search and pagination for student records.
- **Admin Interface**: Easy management of departments, students, subjects, and marks.

## Technologies Used

- **Backend**: Django, Django ORM
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default)
- **Email**: Django Email Backend
- **Others**: Faker for generating demo student details

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/gradesheet-generator.git
    cd gradesheet-generator
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations and start the development server:

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

## Usage

1. **Admin Interface**: Access the admin interface at `/admin` to manage departments, students, subjects, and marks.
2. **Student Portal**: Students can access their gradesheets after OTP verification through the provided URLs.

## Project Structure

- **models.py**: Defines the database models for Department, Student, Subject, SubjectMarks, and ReportCard.
- **admin.py**: Customizes the admin interface for managing the models.
- **views.py**: Contains the logic for handling requests and rendering templates.
- **urls.py**: Defines the URL patterns for routing requests.
- **templates/**: Contains HTML templates for rendering the web pages.

## Models Overview

- **Department**: Stores department information.
- **StudentID**: Unique student identifiers.
- **Subject**: Information about subjects.
- **Student**: Detailed student information including personal details and foreign keys to Department and StudentID.
- **SubjectMarks**: Stores marks for each subject related to students.
- **ReportCard**: Generates and stores report card details including student rank and generation date.

## Admin Interface

The admin interface provides an easy way to manage all the entities within the application. Key functionalities include:

- **List and manage departments**: Add, update, and delete departments.
- **Manage students and their details**: Add, update, and delete student records.
- **Enter subject marks**: Manage marks for each subject per student.
- **Generate report cards**: View and manage report card details.

## Views and URLs

### Key Views

- **get_students**: Lists all students with search and pagination.
- **generate_and_send_otp**: Generates and sends OTP to the student's email.
- **verify_otp**: Verifies the OTP entered by the student.
- **resend_otp**: Resends a new OTP to the student's email.
- **see_marks**: Displays the marks and gradesheet for the verified student.

### URL Patterns

- `/report/`: Includes URL patterns for report-related views.
- `/students/`: Lists all students.
- `/generate_otp/<student_id>/`: Generates OTP for the given student ID.
- `/verify_otp/`: Verifies the OTP entered by the student.
- `/resend_otp/`: Resends OTP to the student.
- `/see_marks/<student_id>/`: Displays the gradesheet for the given student ID.
- `/admin/`: Admin interface.
