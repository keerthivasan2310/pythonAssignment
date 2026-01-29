from collections import deque

def can_stack_cubes(side_lengths):
    """
    Determines if cubes can be stacked such that each cube is smaller 
    than or equal to the one below it.
    """
    d = deque(side_lengths)
    # Start with an infinitely large base
    last_picked = float('inf')
    
    while d:
        # Pick the larger of the two ends
        if d[0] >= d[-1]:
            current = d.popleft()
        else:
            current = d.popright()
            
        # If the current cube is larger than the previous one, stacking fails
        if current > last_picked:
            return "No"
            
        last_picked = current
        
    return "Yes"