Introduction to Django
 Weight: 1
 Project over - took place from Oct 27, 2025 12:00 AM to Nov 3, 2025 12:00 AM
In a nutshell…
0.0/15 mandatory
Final score:  0.0%


Welcome to the “Introduction to Django” project. This project is tailored for you to help you gain hands-on experience with Django, one of the most popular web frameworks for building robust web applications. Throughout this project, you will set up a Django development environment, learn about Django models and ORM, and explore the Django admin interface.

Objectives
Set Up Django Development Environment:

Install Django and create a new Django project.
Familiarize yourself with the project’s default structure and run the development server.
Implementing and Interacting with Django Models:

Create a Django app.
Define Django models with specified attributes.
Perform and document CRUD operations using Django’s ORM via the Django shell.
Utilizing the Django Admin Interface:

Register your models with the Django admin.
Customize the admin interface to enhance the management and visibility of your data.
This structured approach will provide you with a solid foundation in Django, preparing you to develop more complex web applications in the future.

Tasks
0. Introduction to Django Development Environment Setup
mandatory
Score: 0.0% (Checks completed: 0.0%)
Objective: Gain familiarity with Django by setting up a Django development environment and creating a basic Django project. This task aims to introduce you to the workflow of Django projects, including project creation and running the development server.

Task Description:
Install Django and create a new Django project named LibraryProject. This initial setup will serve as the foundation for developing Django applications. You’ll also explore the project’s default structure to understand the roles of various components.

Steps:
Install Django:

Ensure Python is installed on your system.
Install Django using pip: pip install django.
Create Your Django Project:

Create a new Django project by running: django-admin startproject LibraryProject.
Run the Development Server:

Navigate into your project directory (cd LibraryProject).
Create a README.md file inside the LibraryProject.
Start the development server using: python manage.py runserver.
Open a web browser and go to http://127.0.0.1:8000/ to view the default Django welcome page.
Explore the Project Structure:

Familiarize yourself with the created project structure. Pay particular attention to:
settings.py: Configuration for the Django project.
urls.py: The URL declarations for the project; a “table of contents” of your Django-powered site.
manage.py: A command-line utility that lets you interact with this Django project
Repo:

GitHub repository: Alx_DjangoLearnLab
Directory: Introduction_to_Django
   
1. Implementing and Interacting with Django Models
mandatory
Score: 0.0% (Checks completed: 0.0%)
Objective: Demonstrate proficiency in Django by creating a Book model within a Django app, implementing it according to specified attributes, and using Django’s ORM to perform database operations.

Task Description:
For this task, you will develop a Django app named bookshelf within your existing Django project. You will define a Book model with specific attributes and demonstrate basic CRUD operations through the Django shell. This task is structured to ensure consistent implementations suitable for automated checking.

Steps:
Create the bookshelf App:

In your Django project directory, use Django’s command-line utility to generate a new app: python manage.py startapp bookshelf.
Define the Book Model:

Navigate to bookshelf/models.py.
Create a Book class with the following fields:
title: CharField with a maximum length of 200 characters.
author: CharField with a maximum length of 100 characters.
publication_year: IntegerField.
Ensure the model is correctly set up for migrations.

Model Migration:

Prepare your model for database integration by running python manage.py makemigrations bookshelf to create migration files.
Apply migrations to update the database with python manage.py migrate.
Interact with the Model via Django Shell:

Open the Django shell with python manage.py shell and execute CRUD operations:
Create a Book instance.
Retrieve the book you created.
Update the title of the created book.
Delete the book instance.
Perform Specific CRUD Operations in the Django Shell: - Document each operation in separate Markdown files (create.md, retrieve.md, update.md, delete.md) detailing both the Python command used and its output.

Detailed CRUD Operations and Documentation:
Create:

Command: Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.
Document in: create.md
Expected Documentation: Include the Python command and a comment with the expected output noting the successful creation.
Retrieve:

Command: Retrieve and display all attributes of the book you just created.
Document in: retrieve.md
Expected Documentation: Include the Python command and a comment with the expected output showing the details of the book.
Update:

Command: Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.
Document in: update.md
Expected Documentation: Include the Python command and a comment with the expected output showing the updated title.
Delete:

Command: Delete the book you created and confirm the deletion by trying to retrieve all books again.
Document in: delete.md
Expected Documentation: Include the Python command and a comment with the expected output confirming the deletion.
Implementation and Submission Instructions:
Code Implementation: Your models.py file should correctly define the Book model as specified. Ensure that all field types and options are accurately implemented.
Database Operations: Perform and document each CRUD operation in the Django shell. Save your commands and their outputs in a file named CRUD_operations.md.
Repo:

GitHub repository: Alx_DjangoLearnLab
Directory: Introduction_to_Django
   
2. Utilizing the Django Admin Interface
mandatory
Score: 0.0% (Checks completed: 0.0%)
Objective: Gain practical experience with the Django admin interface by configuring the admin to manage the Book model. This task will demonstrate how to use Django’s built-in admin interface to perform data management tasks efficiently.

Task Description:
Enhance your bookshelf app by integrating the Book model with the Django admin interface. Customize the admin display to improve the management and visibility of book data, and document the process to ensure consistent setup and configuration.

Steps:
Register the Book Model with the Django Admin:

Modify bookshelf/admin.py to include the Book model, enabling admin functionalities for it.
Customize the Admin Interface:

Implement custom configurations to display title, author, and publication_year in the admin list view.
Configure list filters and search capabilities to enhance the admin’s usability for Book entries.
Repo:

GitHub repository: Alx_DjangoLearnLab
Directory: Introduction_to_Django