from collections import OrderedDict

def get_word_stats(words):
    """
    Counts distinct words and their occurrences in order of appearance.
    Returns the count of distinct words and a list of their occurrences.
    """
    word_counts = OrderedDict()
    
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
            
    distinct_count = len(word_counts)
    occurrences = list(word_counts.values())
    
    return distinct_count, occurrences