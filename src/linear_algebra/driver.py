from util import get_matrix_determinant

def main():
    try:
        # Read the integer N (dimensions of NxN matrix)
        line = input().strip()
        if not line:
            return
        n = int(line)
        
        # Read N lines of space-separated elements
        matrix_data = []
        for _ in range(n):
            row = list(map(float, input().split()))
            matrix_data.append(row)
        
        # Calculate and print the result
        result = get_matrix_determinant(matrix_data)
        print(result)
            
    except EOFError:
        pass
    except ValueError:
        print("Invalid input format.")

if __name__ == "__main__":
    main()