from src.util import handle_insert, handle_append, handle_remove

def test_insert():
    arr = []
    handle_insert(arr, 0, 10)
    assert arr == [10]

def test_append():
    arr = [5]
    handle_append(arr, 20)
    assert arr == [5, 20]

def test_remove():
    arr = [1, 2, 3, 2]
    handle_remove(arr, 2)
    assert arr == [1, 3, 2]