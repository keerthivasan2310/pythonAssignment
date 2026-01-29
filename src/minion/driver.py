from util import minion_game

def main():
    try:
        s = input().strip()
        if s:
            minion_game(s)
    except EOFError:
        pass

if __name__ == "__main__":
    main()