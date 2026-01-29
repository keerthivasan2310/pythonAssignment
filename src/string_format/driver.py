from util import print_formatted

def main():
    try:
        # Read a single integer denoting n
        line = input().strip()
        if line:
            n = int(line)
            print_formatted(n)
            
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    main()