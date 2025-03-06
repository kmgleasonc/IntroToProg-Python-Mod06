# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Keily Gleason>,<3/1/2025>,<Functions>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
# student_first_name: str = ''  # Holds the first name of a student entered by the user.
# student_last_name: str = ''  # Holds the last name of a student entered by the user.
# course_name: str = ''  # Holds the name of a course entered by the user.
# student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
# csv_data: str = ''  # Holds combined string data separated by a comma.
# json_data: str = ''  # Holds combined string data in a json format.
# file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    # When the program starts, read the file data into table
    # Extract the data from the file
    # Read from the Json file

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        # global file
        # global students

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

# try:
#     file = open(FILE_NAME, "r")
#
#     # CSV Answer
#     # for row in file.readlines():
#     #     # Transform the data from the file
#     #     student_data = row.split(',')
#     #     student_data = {"FirstName": student_data[0],
#     #                     "LastName": student_data[1],
#     #                     "CourseName": student_data[2].strip()}
#     #     # Load it into our collection (list of lists)
#     #     students.append(student_data)
#
#     # JSON Answer
#     students = json.load(file)
#
#     file.close()
# except Exception as e:
#     print("Error: There was a problem with reading the file.")
#     print("Please check that the file exists and that it is in a json format.")
#     print("-- Technical Error Message -- ")
#     print(e.__doc__)
#     print(e.__str__())
# finally:
#     if file.closed == False:
#         file.close()

# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the a menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :return: None
        """
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        # Process the data to create and display a custom message
        print()
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
        print()

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and GPA from the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :return: None
        """

        try:
            # Input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Error: There was a problem with your entered data.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        return students

#  End of function definitions

# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Get new data (and display the change)
        students = IO.input_student_data(student_data=students)
        IO.output_student_courses(student_data=students)  # Added this to improve user experience
        continue

    elif menu_choice == "2":  # Display current data
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "3":  # Save data in a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop

# Present and Process the data
# while (True):
#
#     # Present the menu of choices
#     print(MENU)
#     menu_choice = input("What would you like to do: ")
#
#     # Input user data
#     if menu_choice == "1":  # This will not work if it is an integer!
#
#         try:
#             student_first_name = input("Enter the student's first name: ")
#             if not student_first_name.isalpha():
#                 raise ValueError("The last name should not contain numbers.")
#             student_last_name = input("Enter the student's last name: ")
#             if not student_last_name.isalpha():
#                 raise ValueError("The last name should not contain numbers.")
#             course_name = input("Please enter the name of the course: ")
#             student_data = {"FirstName": student_first_name,
#                             "LastName": student_last_name,
#                             "CourseName": course_name}
#             students.append(student_data)
#             print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
#         except ValueError as e:
#             print(e)  # Prints the custom message
#             print("-- Technical Error Message -- ")
#             print(e.__doc__)
#             print(e.__str__())
#         except Exception as e:
#             print("Error: There was a problem with your entered data.")
#             print("-- Technical Error Message -- ")
#             print(e.__doc__)
#             print(e.__str__())
#         continue
#
#     # Present the current data
#     elif menu_choice == "2":
#
#         # Process the data to create and display a custom message
#         print("-" * 50)
#         for student in students:
#             print(f'Student {student["FirstName"]} '
#                   f'{student["LastName"]} is enrolled in {student["CourseName"]}')
#         print("-" * 50)
#         continue
#
#     # Save the data to a file
#     elif menu_choice == "3":
#
#         try:
#             file = open(FILE_NAME, "w")
#             # CSV answer
#             # for student in students:
#             #     csv_data = f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}\n'
#             #     file.write(csv_data)
#
#             # # JSON answer
#             json.dump(students, file)
#
#             file.close()
#             print("The following data was saved to file!")
#             for student in students:
#                 print(f'Student {student["FirstName"]} '
#                       f'{student["LastName"]} is enrolled in {student["CourseName"]}')
#         except Exception as e:
#             if file.closed == False:
#                 file.close()
#             print("Error: There was a problem with writing to the file.")
#             print("Please check that the file is not open by another program.")
#             print("-- Technical Error Message -- ")
#             print(e.__doc__)
#             print(e.__str__())
#         continue
#
#     # Stop the loop
#     elif menu_choice == "4":
#         break  # out of the loop
#     else:
#         print("Please only choose option 1, 2, or 3")

print("Program Ended")
