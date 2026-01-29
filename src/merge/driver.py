from util import merge_the_tools

def main():
    try:
        # Read the input string s and integer k
        s = input()
        k = int(input())
        
        # Process and print the resulting subsequences
        merge_the_tools(s, k)
            
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    main()