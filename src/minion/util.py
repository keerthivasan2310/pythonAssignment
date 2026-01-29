def minion_game(string):
    """
    Calculates the scores for Stuart and Kevin.
    Stuart: Consonants | Kevin: Vowels
    """
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    length = len(string)

    for i in range(length):
        # Substrings starting at index i
        if string[i] in vowels:
            kevin_score += (length - i)
        else:
            stuart_score += (length - i)

    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")