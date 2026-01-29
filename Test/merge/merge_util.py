# Note: Since merge_the_tools prints output, a helper 
# function or capturing stdout is used for testing.

def get_unique_subsequence(t_i):
    u_i = ""
    for char in t_i:
        if char not in u_i:
            u_i += char
    return u_i

def test_subsequence_logic():
    # Example 1: 'AAA' -> 'A'
    assert get_unique_subsequence("AAA") == "A"
    
    # Example 2: 'BCA' -> 'BCA'
    assert get_unique_subsequence("BCA") == "BCA"
    
    # Example 3: 'DDE' -> 'DE'
    assert get_unique_subsequence("DDE") == "DE"

def test_sample_case():
    # Sample Input: 'AABCAAADA', k=3
    # Segments: 'AAB' -> 'AB', 'CAA' -> 'CA', 'ADA' -> 'AD'
    assert get_unique_subsequence("AAB") == "AB"
    assert get_unique_subsequence("CAA") == "CA"
    assert get_unique_subsequence("ADA") == "AD"