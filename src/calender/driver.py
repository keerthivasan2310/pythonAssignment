from util import get_day_of_week

def main():
    try:
        # Expected input format: MM DD YYYY
        line = input().strip()
        if not line:
            return
            
        m, d, y = map(int, line.split())
        
        result = get_day_of_week(m, d, y)
        print(result)
    except ValueError:
        print("Invalid input format. Please use: MM DD YYYY")

if __name__ == "__main__":
    main()