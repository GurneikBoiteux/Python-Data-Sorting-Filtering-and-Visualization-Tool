# ECOR 1042 Lab 6 - Individual submission for text_UI.
import load_data
import sort
import curve_fit
import histogram
import matplotlib.pyplot as plt

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Gurneik Boiteux"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101340830"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "XXXX"

# ==========================================#
# Place your script for your text_UI after this line
# You are allowed to create auxiliary functions


def textUI() -> None:
    """
    Run the text-based user interface for loading students, sorting, and graphing.
    """
    student_data = []

    while True:
        print("\nL)oad Data")
        print("S)ort Data")
        print("C)urve Fit")
        print("H)istogram")
        print("E)xit")
        user_choice = input("Enter your choice: ").strip().upper()

        if user_choice == "L":
            filename = input("Please enter the name of the file: ")
            attribute = input(
                "Please enter the attribute to use as a filter: ")

            if attribute.upper() != "ALL":
                attribute_value = input(
                    "Please enter the value of the attribute: ")
                try:
                    if attribute in ["Age", "Failures", "Health"]:
                        attribute_value = int(attribute_value)
                    student_data = load_data.load_data(
                        filename, {attribute: attribute_value})
                except:
                    print("Invalid attribute or value.")
                    continue
            else:
                student_data = load_data.load_data(filename, {"All": True})

            if not student_data:
                print("File not loaded. Please, load a file first.")
            else:
                student_data = load_data.add_average(student_data)
                print("Data loaded")

        elif user_choice == "S":
            if not student_data:
                print("File not loaded. Please, load a file first.")
                continue

            valid_attributes = "'Age', 'Failures', 'AvgGrade', 'StudyTime'"
            attribute = input(f"Please enter a valid attribute: ")

            if attribute not in ["Age", "Failures", "AvgGrade", "StudyTime"]:
                print("Invalid command.")
                continue

            order = input(
                "Ascending (A) or Descending (D) order: ").strip().upper()
            if order not in ["A", "D"]:
                print("Invalid command.")
                continue

            display = input(
                "Do you want to display the data?: ").strip().upper()
            sorted_data = sort.sort(student_data, order, attribute)
            student_data = sorted_data

            if display == "Y":
                print("\n<<Data is displayed>>")
                for student in sorted_data:
                    print(student)
            else:
                print("List sorted. <<<You selected not to display>>>")

        elif user_choice == "C":
            if not student_data:
                print("File not loaded. Please, load a file first.")
                continue

            attribute = input(
                "Please enter the attribute you want to use to find the best fit for AvgGrade: ")
            order = input(
                "Please enter the order of the polynomial to be fitted: ")
            try:
                order = int(order)
                equation = curve_fit.curve_fit(
                    student_data, attribute, order)
                print(equation)
            except ValueError:
                print("Invalid command.")

        elif user_choice == "H":
            if not student_data:
                print("File not loaded. Please, load a file first.")
                continue

            attribute = input(
                "Please enter the attribute you want to use for plotting: ")
            print("\n<<The Histogram is displayed>>")
            histogram.histogram(student_data, attribute)
            plt.show()

        elif user_choice == "E":
            break

        else:
            print("Invalid command.")


if __name__ == "__main__":
    textUI()
