# ECOR 1042 Lab 6 - Individual submission for histogram.

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "XXXX"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "XXXXXXXXXX"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-042"

# ==========================================#
# Place your histogram function after this line
import matplotlib.pyplot as plt


def histogram(students: list[dict], attribute: str) -> None:
    values = {}
    value_type = None

    for student in students:
        the_value = student.get(attribute)
        if the_value is None:
            continue

        value_type = type(the_value)
        if the_value in values:
            values[the_value] += 1
        else:
            values[the_value] = 1

    if value_type == str:
        fig = plt.figure()
        plt.bar(values.keys(), values.values(),
                color='red', edgecolor='black')
        plt.xlabel(attribute)
        plt.ylabel("Number of students")
        plt.title(f'Histogram of {attribute}')
        plt.show()
        return -1

    elif value_type == int or float:
        value_list = []
        for student in students:
            if attribute in student:
                value_list.append(student[attribute])

        if len(value_list) == 0:
            print("Invalid Command")
            return

        range_ = max(value_list) - min(value_list)
        interval = range_ / 10 if range_ != 0 else 1
        bins = [0] * 10

        for val in value_list:
            index = min(int((val - min(value_list)) / interval), 9)
            bins[index] += 1

        x_labels = [
            f"{round(min(value_list) + i * interval)}" for i in range(10)]

        fig = plt.figure()
        plt.bar(x_labels, bins, color='red', edgecolor='black')
        plt.xlabel(attribute)
        plt.ylabel("Number of students")
        plt.title(f'Histogram of {attribute}')
        plt.show()
        return max(value_list)

# Do NOT include a main script in your submission
