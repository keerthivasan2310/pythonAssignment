def process_commands(commands):
    lst = []
    outputs = []

    for command in commands:
        parts = command.split()

        if parts[0] == "insert":
            lst.insert(int(parts[1]), int(parts[2]))

        elif parts[0] == "print":
            outputs.append(str(lst))

        elif parts[0] == "remove":
            lst.remove(int(parts[1]))

        elif parts[0] == "append":
            lst.append(int(parts[1]))

        elif parts[0] == "sort":
            lst.sort()

        elif parts[0] == "pop":
            lst.pop()

        elif parts[0] == "reverse":
            lst.reverse()

    return outputs
