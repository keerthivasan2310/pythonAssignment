from datetime import datetime

def time_delta(t1, t2):
    """
    Calculates the absolute difference in seconds between two 
    timestamp strings with timezones.
    Format: Day dd Mon yyyy hh:mm:ss +xxxx
    """
    # Directive for: Day dd Mon yyyy hh:mm:ss +xxxx
    time_format = '%a %d %b %Y %H:%M:%S %z'
    
    # Parse the strings into datetime objects
    dt1 = datetime.strptime(t1, time_format)
    dt2 = datetime.strptime(t2, time_format)
    
    # Calculate absolute difference in seconds
    return int(abs((dt1 - dt2).total_seconds()))