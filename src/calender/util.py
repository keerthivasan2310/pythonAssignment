import calendar

def get_day_of_week(month, day, year):
    """
    Takes MM, DD, YYYY and returns the day name in uppercase.
    """
    day_index = calendar.weekday(year, month, day)
    return calendar.day_name[day_index].upper()