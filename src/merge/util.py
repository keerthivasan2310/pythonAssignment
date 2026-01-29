def merge_the_tools(string, k):
    """
    Splits a string into n/k substrings and removes duplicate 
    characters from each while maintaining original order.
    """
    # Iterate through the string in chunks of size k
    for i in range(0, len(string), k):
        t_i = string[i : i + k]
        u_i = ""
        
        # Remove duplicate occurrences from the current substring
        for char in t_i:
            if char not in u_i:
                u_i += char
        
        # Print each unique subsequence on a new line
        print(u_i)