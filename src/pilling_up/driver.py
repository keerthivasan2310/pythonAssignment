from util import can_stack_cubes

def main():
    try:
        # Read the number of test cases
        line = input().strip()
        if not line:
            return
        t = int(line)
        
        for _ in range(t):
            # Read n (number of cubes) - not strictly needed for logic but part of input
            _ = input()
            # Read the side lengths
            side_lengths = list(map(int, input().split()))
            
            # Print the result for each test case
            print(can_stack_cubes(side_lengths))
            
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    main()