import numpy

def get_matrix_determinant(matrix_data):
    """
    Calculates the determinant of a square matrix using numpy.linalg.det.
    """
    # Convert list of lists into a numpy array
    my_array = numpy.array(matrix_data, float)
    
    # Calculate determinant
    determinant = numpy.linalg.det(my_array)
    
    # Return rounded to 2 decimal places per the task requirement
    return round(float(determinant), 2)