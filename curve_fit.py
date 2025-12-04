# ECOR 1042 Lab 6 - Individual submission for curve_fit function.

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin) STUDENT NAMES X'D OUT FOR CONFIDENTIALITY
__author__ = "XXXX"

# Update "" with your student number (e.g., 100100100) STUDENT NUMBERS X'D OUT FOR CONFIDENTIALITY
__student_number__ = "XXXXXXXXX"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-042"

# ==========================================#
# Place your curve_fit function after this line
import matplotlib.pyplot as plt
import numpy as np


def curve_fit(arr: [dict], attribute: str, degree: int) -> str:
    """
    """

    x = []

    for i in range(len(arr)):
        x.append(arr[i][attribute])

    new_x = (list(set(x)))

    y = []
    for val in new_x:
        total = 0
        count = 0
        for i in range(len(arr)):
            if arr[i][attribute] == val:
                total += arr[i]["AvgGrade"]
                count += 1

        if count > 0:
            y.append(total / count)
        else:
            break

    if degree >= len(new_x):
        degree = len(new_x) - 1

    coeff = np.polyfit(new_x, y, degree)

    equation = "y = "
    power = degree
    for n in coeff:
        n = round(n, 2)
        if power > 1:
            equation += f"{n}x^{power} + "
        elif power == 1:
            equation += f"{n}x + "
        else:
            equation += f"{n}"
        power -= 1

    return equation.strip(" + ")


# Do NOT include a main script in your submission
