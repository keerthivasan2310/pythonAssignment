def calculate_happiness(n_array, set_a, set_b):
    """
    Calculates total happiness by checking array elements against 
    two sets, A and B.
    """
    happiness = 0
    
    # Membership testing in a set is O(1)
    for num in n_array:
        if num in set_a:
            happiness += 1
        elif num in set_b:
            happiness -= 1
            
    return happiness