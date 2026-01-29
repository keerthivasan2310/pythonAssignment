from util import execute_list_op

def main():
    try:
        # Read the number of commands
        n = int(input())
        my_list = []
        
        # Directly pass the input to the operation function
        for _ in range(n):
            execute_list_op(my_list, input())
            
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    main()