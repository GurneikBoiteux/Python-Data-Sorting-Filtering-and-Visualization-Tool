# ECOR 1042 Lab 5 - Team submission.
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Gurneik Boiteux, XXXX, XXXX, XXXX"

# Update "" with your team (e.g. T102)
__team__ = "XXXX"

# ==========================================#
# Place your sort_students_age_bubble function after this line


def sort_students_age_bubble(users_list: list[dict], order: str) -> str:
    """
    return a string and sort the Age in either ascending or descending order depending on what is asked. 


    >>> a = [] 
    >>> sort_students_age_bubble(a, "A") 
    Empty list. 

    >>> a = [{"Age":12,"School":"GP"},{"Age":13,"School":"MS"}] 
    >>> sort_students_age_bubble( a, "D") 
    a = [{"Age": 13, "School":"MS"}, {"Age":12, "School":"GP"}]
    List sorted. 


    >>> a = [{"School":"GD"}, {"School":"MF"}] 
    >>> sort_students_age_bubble(a, "D") 
    List not sorted. Age key not present. 
    """

    if len(users_list) == 0:
        return "Empty list."

    elif "Age" not in users_list[0]:
        return "List not sorted. Age key not present."

    if order == "D":
        swap = True
        while swap:
            swap = False
            for i in range(len(users_list) - 1):
                if users_list[i]["Age"] < users_list[i + 1]["Age"]:
                    users_list[i], users_list[i +
                                              1] = users_list[i + 1], users_list[i]
                    swap = True
        return "List sorted."

    elif order == "A":
        swap = True
        while swap:
            swap = False
            for i in range(len(users_list) - 1):
                if users_list[i]["Age"] > users_list[i + 1]["Age"]:
                    users_list[i], users_list[i +
                                              1] = users_list[i + 1], users_list[i]
                    swap = True
        return "List sorted."

    else:
        return "Invalid sort order."


# ==========================================#
# Place your sort_students_time_selection function after this line


def sort_students_time_selection(student_list: list[dict], order: str) -> str:
    """
    Return string and sort list of student dictionaries using selection sort.
    If there are no students in student_list then the function returns 
    "Empty list." If there is no StudyTime key in the dictionaries the function
    returns "List not sorted. StudyTime key not present."

    >>>sort_students_time_selection([{"School": "GP", "StudyTime": 10}, {"School": "MS", "StudyTime": 6}], "A")
    'List Sorted'
    >>>sort_students_time_selection([], "A")
    'Empty list.'
    >>>sort_students_time_selection([{"School": "GP", "Age": 19}, {"School": "MS", "Age": 18}], "D")
    'List not sorted. StudyTime key not present.'
    """
    if not student_list:
        return "Empty list."

    if not all("StudyTime" in student for student in student_list):
        return "List not sorted. StudyTime key not present."

    n = len(student_list)
    for i in range(n):
        selected_idx = i
        for j in range(i + 1, n):
            if (order == "A" and student_list[j]["StudyTime"] < student_list[selected_idx]["StudyTime"]) or \
               (order == "D" and student_list[j]["StudyTime"] > student_list[selected_idx]["StudyTime"]):
                selected_idx = j

        if selected_idx != i:
            student_list[i], student_list[selected_idx] = student_list[selected_idx], student_list[i]

    return "List sorted."

# ==========================================#
# Place your sort_students_avg_insertion function after this line


def sort_students_avg_insertion(not_sorted_list: list[dict], ascending_or_descending: str) -> str:
    """Return a string whether the list is sorted, empty list or AvgGrade key is not present. It uses insertion sort algorithm and sort the list of dictionaries based on AvgGrade either ascending or descending.

    >>> a = []
    >>> sort_students_avg_insertion(a, "D")
    Empty list.
    >>> b = [{"AvgGrade":7.2,"School":"GP"}, {"AvgGrade":9.1,"School":"MS"}]
    >>> sort_students_avg_insertion( b, "D")
    List sorted.
    >>> c = [{"School":"GP"}, {"School":"MS"}]
    >>> sort_students_avg_insertion(c, "A")
    List not sorted. AvgGrade key not present"""

    letter = ascending_or_descending.lower()

    if not_sorted_list == []:
        return ("Empty list.")

    try:

        if letter == "a":
            for i in range(1, len(not_sorted_list)):
                key = not_sorted_list[i]

                j = i - 1
                while j >= 0 and key["AvgGrade"] < not_sorted_list[j]["AvgGrade"]:
                    not_sorted_list[j + 1] = not_sorted_list[j]
                    j -= 1
                not_sorted_list[j + 1] = key
            return ("List sorted.")

        else:
            for i in range(1, len(not_sorted_list)):
                key = not_sorted_list[i]

                j = i - 1
                while j >= 0 and key["AvgGrade"] > not_sorted_list[j]["AvgGrade"]:
                    not_sorted_list[j + 1] = not_sorted_list[j]
                    j -= 1
                not_sorted_list[j + 1] = key
            return ("List sorted.")

    except:
        return ("List not sorted. AvgGrade key not present.")
# ==========================================#
# Place your sort_students_failures_bubble function after this line


def sort_students_failures_bubble(arr: list[dict], order: str) -> str:
    """Returns a string after it sorts a list of students by the number of failures.

    If the list is empty, the function returns the string 'Empty list.'

    If the "Failures" key is missing, the function returns the string 'List not sorted. Failures key not present.'

    Otherwise, the function sorts the list and returns the string 'List sorted.'



    arr: the list of student dictionaries.

    order: "A" for ascending and "D" for descending.



    >>> a = []

    >>> sort_students_failures_bubble(a, "A")

    'Empty list.'



    >>> a = [{"Failures":19,"School":"GP"},{"Failures":10,"School":"MS"}]

    >>> sort_students_failures_bubble(a, "A")

    'List sorted.'



    >>> a = [{"School":"GP"}, {"School":"MS"}]

    >>> sort_students_failures_bubble(a, "A")

    'List not sorted. Failures key not present.'

    """

    if len(arr) == 0:

        return "Empty list."

    elif "Failures" not in arr[0]:

        return "List not sorted. Failures key not present."

    swap = True

    while swap:

        swap = False

        for i in range(len(arr) - 1):

            if order == "A" and arr[i]["Failures"] > arr[i + 1]["Failures"]:

                aux = arr[i]

                arr[i] = arr[i + 1]

                arr[i + 1] = aux

                swap = True

            elif order == "D" and arr[i]["Failures"] < arr[i + 1]["Failures"]:

                aux = arr[i]

                arr[i] = arr[i + 1]

                arr[i + 1] = aux

                swap = True

    return "List sorted."
# ==========================================#
# Place your sort function after this line


def sort(student_list: list[dict], order: str, attribute: str) -> str:
    """
    Returns string after sorting list based on given parameters

    Preconditions: attribute must be a valid input parameter:("Age", "StudyTime", "AvgGrade", "Failures").

    >>>sort([{"Age": 20, "StudyTime": 5, "AvgGrade": 85, "Failures": 1}, {"Age": 18, "StudyTime": 10, "AvgGrade": 90, "Failures": 0}], "A", "Age")
    'List sorted.'

    >>>sort([], "A", "StudyTime")
    'Empty list.'

    >>>sort([{"Age": 22, "StudyTime": 6}, {"Age": 19, "StudyTime": 4}], "D", "Blah")
    'Invalid input, the list cannot be sorted by Blah.'

    """
    if attribute == "Age":
        return sort_students_age_bubble(student_list, order)
    elif attribute == "StudyTime":
        return sort_students_time_selection(student_list, order)
    elif attribute == "AvgGrade":
        return sort_students_avg_insertion(student_list, order)
    elif attribute == "Failures":
        return sort_students_failures_bubble(student_list, order)
    else:
        return f"Invalid input, the list cannot be sorted by {attribute}."

# Do NOT include a main script in your submission
