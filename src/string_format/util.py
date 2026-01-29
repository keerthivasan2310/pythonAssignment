def get_formatted_line(i, width):
    """
    Returns a single space-separated string containing decimal, octal, 
    hexadecimal (capitalized), and binary values of i, all right-aligned 
    to the specified width.
    """
    # Convert i to various formats and remove the prefix (0o, 0x, 0b)
    dec = str(i)
    octal = oct(i)[2:]
    hex_val = hex(i)[2:].upper()
    binary = bin(i)[2:]
    
    # Format each value to match the width of the binary value of 'number'
    return f"{dec.rjust(width)} {octal.rjust(width)} {hex_val.rjust(width)} {binary.rjust(width)}"

def print_formatted(number):
    """
    Iterates from 1 to number and prints the formatted values for each.
    """
    # The padding width is determined by the length of the binary representation of 'number'
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        print(get_formatted_line(i, width))