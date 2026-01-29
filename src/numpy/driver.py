from util import get_numpy_math_ops

def main():
    try:
        # Read the space-separated numbers from input
        line = input().strip()
        if not line:
            return
            
        # Convert input string to a list of floats
        array_data = list(map(float, line.split()))
        
        # Get results from util
        floor_res, ceil_res, rint_res = get_numpy_math_ops(array_data)
        
        # Print results as required
        print(floor_res)
        print(ceil_res)
        print(rint_res)
            
    except EOFError:
        pass
    except ValueError:
        print("Invalid input. Please provide space-separated numbers.")

if __name__ == "__main__":
    main()