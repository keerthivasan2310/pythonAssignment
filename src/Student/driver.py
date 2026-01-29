from util import calculate_average

def main():
    try:
        # Read total number of students
        line = input().strip()
        if not line:
            return # Exit quietly if input is empty
            
        n = int(line)
        
        # Read the column names (e.g., ID MARKS NAME CLASS)
        columns = input().split()
        
        # Collect the next N lines of data
        data_lines = []
        for _ in range(n):
            data_lines.append(input().strip())
        
        # Calculate and print the result
        avg = calculate_average(n, columns, data_lines)
        print(f"{avg:.2f}")
        
    except EOFError:
        pass
    except ValueError as e:
        print(f"Error: Expected a number for the student count, but got something else.")

if __name__ == "__main__":
    main()