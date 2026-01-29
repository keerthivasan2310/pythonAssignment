import numpy

# Setting legacy print options to match HackerRank's expected output format
numpy.set_printoptions(legacy='1.13')

def get_numpy_math_ops(array_data):
    """
    Converts a list of floats to a numpy array and performs
    floor, ceil, and rint operations.
    """
    my_array = numpy.array(array_data, float)
    
    # Return a tuple of the three operations
    return (
        numpy.floor(my_array),
        numpy.ceil(my_array),
        numpy.rint(my_array)
    )