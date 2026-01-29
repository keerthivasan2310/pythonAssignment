from util import get_word_stats

def main():
    try:
        # Read the number of words
        line = input().strip()
        if not line:
            return
        n = int(line)
        
        # Collect each word provided in the next n lines
        words = []
        for _ in range(n):
            words.append(input().strip())
        
        # Process the words
        distinct_count, occurrences = get_word_stats(words)
        
        # Output result: first line is count of distinct words
        print(distinct_count)
        # Second line is space-separated occurrences
        print(*(occurrences))
        
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    main()