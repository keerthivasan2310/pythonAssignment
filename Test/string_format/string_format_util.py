from src.util import get_formatted_line

def test_single_digit_format():
    # For n=2, binary '10' has width 2. Decimal 1 should be ' 1'
    assert get_formatted_line(1, 2) == " 1  1  1  1"

def test_hex_capitalization():
    # Decimal 10 is 'A' in Hexadecimal
    # width of 5 (matching binary '10001' for n=17)
    line = get_formatted_line(10, 5)
    parts = line.split()
    assert parts[2] == "A"

def test_sample_output_row():
    # Test row 17 from sample output with width 5
    # 17 (dec), 21 (oct), 11 (hex), 10001 (bin)
    expected = "   17    21    11 10001"
    assert get_formatted_line(17, 5) == expected    