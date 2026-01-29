from src.util import execute_list_op

def test_list_flow():
    arr = []
    execute_list_op(arr, "append 1")
    execute_list_op(arr, "append 2")
    execute_list_op(arr, "insert 1 3")
    # Expected list after operations: [1, 3, 2]
    assert arr == [1, 3, 2]

def test_list_sort_reverse():
    arr = [1, 3, 2]
    execute_list_op(arr, "sort")
    assert arr == [1, 2, 3]
    execute_list_op(arr, "reverse")
    assert arr == [3, 2, 1]

def test_list_pop_remove():
    arr = [3, 2, 1]
    execute_list_op(arr, "remove 2")
    assert arr == [3, 1]
    execute_list_op(arr, "pop")
    assert arr == [3]