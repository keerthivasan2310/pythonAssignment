from src.util import process_commands


def test_sample_case():
    commands = [
        "insert 0 5",
        "insert 1 10",
        "insert 0 6",
        "print",
        "remove 6",
        "append 9",
        "append 1",
        "sort",
        "print",
        "pop",
        "reverse",
        "print"
    ]

    result = process_commands(commands)

    assert result == [
        "[6, 5, 10]",
        "[1, 5, 9, 10]",
        "[9, 5, 1]"
    ]


def test_append_and_print():
    commands = [
        "append 3",
        "append 2",
        "print"
    ]

    result = process_commands(commands)
    assert result == ["[3, 2]"]


def test_insert_only():
    commands = [
        "insert 0 1",
        "insert 1 2",
        "insert 2 3",
        "print"
    ]

    result = process_commands(commands)
    assert result == ["[1, 2, 3]"]
