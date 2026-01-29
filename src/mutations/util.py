def mutate_string(string, position, character):
    """
    Changes the character at a given index and returns the modified string.
    Uses string slicing: string[:position] + character + string[position+1:]
    """
    # Strings are immutable; we recreate it by joining slices around the index
    return string[:position] + character + string[position+1:]