from util import process_commands

def main():
    n = int(input())
    commands = []

    for _ in range(n):
        commands.append(input())

    result = process_commands(commands)

    for output in result:
        print(output)


if __name__ == "__main__":
    main()
