from datetime import datetime

def get_time_delta(t1, t2):
    """
    Parses two timestamp strings and returns the absolute 
    difference in seconds as a string.
    Format: Day dd Mon yyyy hh:mm:ss +xxxx
    """
    # Directive for: Day dd Mon yyyy hh:mm:ss +xxxx
    time_format = '%a %d %b %Y %H:%M:%S %z'
    
    # Parse strings into timezone-aware datetime objects
    dt1 = datetime.strptime(t1, time_format)
    dt2 = datetime.strptime(t2, time_format)
    
    # Calculate absolute difference in seconds
    return str(int(abs((dt1 - dt2).total_seconds())))