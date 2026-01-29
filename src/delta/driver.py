from util import time_delta

def main():
    try:
        # Read the number of test cases
        line = input().strip()
        if not line:
            return
            
        t = int(line)
        
        for _ in range(t):
            t1 = input().strip()
            t2 = input().strip()
            
            result = time_delta(t1, t2)
            print(result)
            
    except EOFError:
        pass
    except ValueError:
        print("Invalid input. Please provide the number of test cases followed by timestamps.")

if __name__ == "__main__":
    main()