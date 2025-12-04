# ECOR 1042 Lab 3 - Team submission.
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work STUDENT NAMES X'D OUT FOR CONFIDENTIALITY
__author__ = "Gurneik Boiteux, XXXX, XXXX, XXXX"

# Update "" with your team (e.g. T102)
__team__ = "T042"

# ==========================================#
# Place your student_school_list function after this line


def student_school_list(filename: str, school_name: str) -> list:
    """return a list of dictionaries contaning all the students from a specfied school
    preconditions: must input one of the given names of the schools

    >>>student_school_list("student-mat.csv", "GP")
    [{'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, {'ID': 2, 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 4, 'FallGrade': 5, 'WinterGrade': 5},.....  
    >>>student_school_list("student-mat.csv", "MB")
    [{'ID': 80, 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 12, 'FallGrade': 5, 'WinterGrade': 5}, {'ID': 81, 'Age': 15, 'StudyTime': 1, 'Failures': 0, 'Health': 3, 'Absences': 2, 'FallGrade': 10, 'WinterGrade': 12},.....  
    >>>student_school_list("student-mat.csv", "AB")
    []
    """
    students = []
    file = open(filename, "r")
    for line in file:
        header = line.strip().split(",")
        break
    if not header:
        return []
    school = header.index("School")
    for line in file:
        values = line.strip().split(",")
        if len(values) != len(header) or values[school] != school_name:
            continue
        student = {header[i]: values[i]
                   for i in range(len(header)) if i != school}
        for key in student:
            try:
                student[key] = float(
                    student[key]) if "." in student[key] else int(student[key])
            except ValueError:
                students_dict[key] = value
        students.append(student)
    file.close()
    return students

# ==========================================#
# Place your student_health_list function after this line


def student_health_list(file_name: str, health_value: int) -> list:
    """Return a list of the students with the corresponding health value
    given to the function

    >>>student_health_list("student-mat.csv", 2)
    [{'School': 'GP', 'ID': 11, 'Age': 15, 'StudyTime': 2, 'Failures': 0,
        'Absences': 0, 'FallGrade': 10, 'WinterGrade': 8},
        {another example}
        ...
    ]
    >>>student_health_list("student-mat.csv", -10)
    []
    >>>student_health_list("student-mat.csv", 5)
    [{'School': 'GP', 'ID': 4, 'Age': 15, 'StudyTime': 3, 'Failures': 0,
        'Absences': 2, 'FallGrade': 15, 'WinterGrade': 14},
        {another}
        ...
    ]
    """
    file = open(file_name, 'r')
    lines = [line.strip().split(',') for line in file]

    headers, rows = lines[0], lines[1:]
    health_index = headers.index('Health')

    result = []
    for row in rows:
        if int(row[health_index]) == health_value:
            student = {headers[i]: int(row[i]) if row[i].isdigit() else float(row[i]) if '.' in row[i] else row[i]
                       for i in range(len(headers)) if i != health_index}
            result.append(student)

    file.close()
    return result

# ==========================================#
# Place your student_age_list function after this line


def student_age_list(filename: str, age: int) -> list[str]:
    """Return a list of students with the same age.
    Precondition: the age can't be negative and the age can't be float.
    >>> student_age_list('student-mat.csv', 15)
    [ {'School': 'GP', 'ID': 201, 'StudyTime': 4.0, 'Failures': 3, 'Health': 3,
    'Absences': 6, 'FallGrade': 7, 'WinterGrade': 8},
    {another element},
    …
    ]
    >>> student_age_list('student-mat.csv', 0)
    []"""

    infile = open(filename, 'r')
    student_info_list = []
    count = 0

    for line in infile:
        if count == 0:
            headers = line.strip().split(',')
            count += 1
        else:
            data = line.strip().split(',')
            student_age = data[2]
            if student_age == str(age):
                student_info = {
                    headers[0]: data[0],
                    headers[1]: int(data[1]),
                    headers[3]: float(data[3]),
                    headers[4]: int(data[4]),
                    headers[5]: int(data[5]),
                    headers[6]: int(data[6]),
                    headers[7]: int(data[7]),
                    headers[8]: int(data[8])
                }
                student_info_list.append(student_info)
            count += 1
    infile.close()
    return student_info_list

# ==========================================#
# Place your student_failures_list function after this line


def student_failures_list(filename: str, failures: int) -> list:
    """Returns a list of students (each student stored as a dictionary) with the same amount of failures as the input parameter.
    filename: the name of the file where the data is stored.
    failures: the number of failures
    Precondition: entry cannot be a duplicate entry.
    >>> student_failures_list('student-mat.csv', 15)
    []
    >>> student_failures_list('student-mat.csv', 0)
    [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, {another element}, ...
    >>> student_failures_list('student-mat.csv', 2)
    [{'School': 'GP', 'ID': 26, 'Age': 16, 'StudyTime': 1.5, 'Health': 5, 'Absences': 14, 'FallGrade': 6, 'WinterGrade': 9}, {another element}, ...

    """

    students = []
    file = open(filename, 'r')
    for line in file:
        headers = line.strip().split(',')
        break
    failures_index = headers.index("Failures")

    for line in file:
        values = line.strip().split(',')
        if values[failures_index] == str(failures):
            student = {headers[i]: int(values[i]) if values[i].isdigit() else float(
                values[i]) if '.' in values[i] else values[i] for i in range(len(headers)) if i != failures_index}
            students.append(student)
    file.close()
    return students

# ==========================================#
# Place your load_data function after this line


def load_data(file_name: str, filter_dict) -> list:
    """Return a list of dictionaries for the specified filter given by the user

    >>>load_data("student-mat.csv", {"Failures": 0})
    [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6},
    ...]
    >>>load_data("student-mat.csv", {"All": 3})
    [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6},
    ...]
    >>>load_data("student-mat.csv", {"G1": 20})
    []
    """
    key, value = list(filter_dict.items())[0]
    keys_valid = {
        'School': student_school_list,
        'Age': student_age_list,
        'Health': student_health_list,
        'Failures': student_failures_list
    }

    if key == 'All':
        file = open(file_name, 'r')
        lines = [line.strip().split(',') for line in file]
        file.close()

        headers, rows = lines[0], lines[1:]
        return [{headers[i]: int(row[i]) if row[i].isdigit() else float(row[i]) if '.' in row[i] else row[i] for i in range(len(headers))} for row in rows]

    if key in keys_valid:
        return keys_valid[key](file_name, value)

    return []

# ==========================================#
# Place your add_average function after this line


def add_average(students: list[dict]) -> list[dict]:
    """Return the average grade of a student and add it to the list of dictionaries as "AvgGrade".
    Precondition: The student dictionary should contain "FallGrade" and "WinterGrade" as floats or integers.
    >>> add_average([ {'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 5, 'WinterGrade': 6}, {another element}, … ] )
    [ {'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 5, 'WinterGrade': 6, 'AvgGrade':5.50}, {another element}, … ]
    >>> add_average([ {'School': 'MB', 'ID': 102, 'Age': 16, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 0, 'FallGrade': 16, 'WinterGrade': 17}, {another element}, … ] )
    [ {'School': 'MB', 'ID': 102, 'Age': 16, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 0, 'FallGrade': 16, 'WinterGrade': 17, 'AvgGrade':16.5}, {another element}, … ]
    >>> add_average([ {'School': 'CF', 'ID': 223, 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'FallGrade': 16, 'WinterGrade': 16}, {another element}, … ] )
    [ {'School': 'CF', 'ID': 223, 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'FallGrade': 16, 'WinterGrade': 16, 'AvgGrade':16.0}, {another element}, … ]
    """

    for grade in students:
        avg_grade = (float(grade['FallGrade']) +
                     float(grade['WinterGrade'])) / 2
        grade['AvgGrade'] = round(avg_grade, 2)
    return students

# Do NOT include a main script in your submission
