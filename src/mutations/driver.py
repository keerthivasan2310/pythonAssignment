from util import mutate_string

def main():
    try:
        # Read the initial string
        s = input()
        
        # Read position and character separated by a space
        i, c = input().split()
        
        # Perform mutation
        s_new = mutate_string(s, int(i), c)
        
        # Print the altered string
        print(s_new)
            
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    main()