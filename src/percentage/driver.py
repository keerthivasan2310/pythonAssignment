from util import calculate_average

def main():
    try:
        # Read the number of student records
        n = int(input())
        student_marks = {}

        # Fill the dictionary with name as key and list of marks as values
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores

        # Read the name to query
        query_name = input()

        result = calculate_average(student_marks, query_name)

        if result is not None:
            # Print average showing 2 places after the decimal
            print("{:.2f}".format(result))
            
    except EOFError:
        pass

if __name__ == "__main__":
    main()