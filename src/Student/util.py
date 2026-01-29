from collections import namedtuple

def calculate_average(n, columns, data_lines):
    """
    Uses namedtuple to parse student data and calculate the average marks.
    """
    # Create the namedtuple class based on the column headers provided
    Student = namedtuple('Student', columns)
    
    total_marks = 0
    for line in data_lines:
        # Split the line and expand it into the Student namedtuple
        student = Student(*line.split())
        total_marks += int(student.MARKS)
    
    # Return the average rounded to 2 decimal places
    return total_marks / n