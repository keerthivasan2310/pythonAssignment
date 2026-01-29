from src.util import calculate_average

def test_average_calculation():
    # Example: (67 + 68 + 69) / 3 = 68.0
    data = {"Krishna": [67, 68, 69]}
    assert calculate_average(data, "Krishna") == 68.0

def test_decimal_average():
    # Example: (25 + 26.5 + 28) / 3 = 26.5
    data = {"Harsh": [25, 26.5, 28]}
    assert calculate_average(data, "Harsh") == 26.5

def test_student_missing():
    data = {"Arjun": [70, 98, 63]}
    assert calculate_average(data, "Malika") is None