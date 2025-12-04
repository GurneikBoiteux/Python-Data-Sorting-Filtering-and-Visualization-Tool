# ECOR 1042 Lab 6 - Individual submission for batch_UI.

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "XXXX"

# Update "" with your student number (e.g., 100100100) STUDENT NUMBERS X'D OUT FOR CONFIDENTIALITY
__student_number__ = "XXXXXXXXX"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "XXXX"

# ==========================================#
# Place your script for your batch_UI after this lin
import load_data
import sort
import curve_fit
import histogram


def batch_ui():

    file_name = input("Please enter the name of the file:\n")

    try:

        command_file = open(file_name, 'r')

        data = None

        for line in command_file:

            parts = line.strip().split(';')

            command = parts[0].strip().upper()

            if command == 'L':

                filename = parts[1].strip()

                attribute = parts[2].strip()

                value = parts[3].strip()

                data = load_data.load_data(filename, {attribute: value})

                if data:

                    print("Data loaded")

                else:

                    print("Data could not be loaded")

            elif command == 'S':

                if data is None:

                    print("File not loaded. Please, load a file first.")

                    continue

                attribute = parts[1].strip()

                order = parts[2].strip().upper()

                display = parts[3].strip().upper()

                data = sort.sort_data(data, attribute, order)

                if display == 'Y':

                    for d in data:

                        print(d)

                else:

                    print("List sorted. <<<You selected not to display>>>")

            elif command == 'C':

                if data is None:

                    print("File not loaded. Please, load a file first.")

                    continue

                attribute = parts[1].strip()

                order = int(parts[2].strip())

                equation = curve_fit.curve_fit(data, attribute, order)

                print(equation)

            elif command == 'H':

                if data is None:

                    print("File not loaded. Please, load a file first.")

                    continue

                attribute = parts[1].strip()

                histogram.histogram(data, attribute)

            elif command == 'E':

                print("Exiting program.")

                break

            else:

                print("Invalid command.")

        command_file.close()

    except FileNotFoundError:

        print("File not found.")


if __name__ == "__main__":
    batch_ui()
# You are allowed to create auxiliary functions


