def calculate_average(student_marks, query_name):
    """
    Calculates the average of the marks for the student name provided.
    """
    if query_name not in student_marks:
        return None

    scores = student_marks[query_name]
    # Calculate average: (sum of scores) / (number of scores)
    avg = sum(scores) / len(scores)
    return avg