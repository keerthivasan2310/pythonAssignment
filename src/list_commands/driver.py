from util import handle_insert, handle_remove, handle_append

def main():
    n = int(input())  # Number of commands
    result_list = []

    for _ in range(n):
        # Split input into command and arguments
        input_data = input().split()
        command = input_data[0]

        if command == "insert":
            handle_insert(result_list, int(input_data[1]), int(input_data[2]))
        elif command == "append":
            handle_append(result_list, int(input_data[1]))
        elif command == "remove":
            handle_remove(result_list, int(input_data[1]))
        elif command == "print":
            print(result_list)
        elif command == "sort":
            result_list.sort()
        elif command == "pop":
            result_list.pop()
        elif command == "reverse":
            result_list.reverse()

if __name__ == "__main__":
    main()