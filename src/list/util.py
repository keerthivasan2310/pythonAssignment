def execute_list_op(my_list, raw_input):
    """
    Parses the raw input string and executes the command on the list.
    """
    parts = raw_input.split()
    cmd = parts[0]
    
    if cmd == "insert":
        my_list.insert(int(parts[1]), int(parts[2]))
    elif cmd == "print":
        print(my_list)
    elif cmd == "remove":
        my_list.remove(int(parts[1]))
    elif cmd == "append":
        my_list.append(int(parts[1]))
    elif cmd == "sort":
        my_list.sort()
    elif cmd == "pop":
        my_list.pop()
    elif cmd == "reverse":
        my_list.reverse()