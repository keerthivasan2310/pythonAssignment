from itertools import combinations

def calculate_probability(n, letters, k):
    """
    Calculates the probability that at least one of the K indices 
    selected from the list contains the letter 'a'.
    """
    # Create a list of indices (1-based or 0-based both work)
    indices = list(range(1, n + 1))
    
    # Find all possible combinations of K indices
    all_combos = list(combinations(indices, k))
    
    # Identify which indices in the original list contain 'a'
    # Use 1-based indexing to match the combinations
    target_indices = [i + 1 for i, char in enumerate(letters) if char == 'a']
    
    # Count how many combinations contain at least one target index
    favorable_outcome = 0
    for combo in all_combos:
        if any(idx in target_indices for idx in combo):
            favorable_outcome += 1
            
    # Probability = Favorable Outcomes / Total Outcomes
    return favorable_outcome / len(all_combos)