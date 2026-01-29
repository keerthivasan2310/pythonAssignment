from src.util import mutate_string

def test_basic_mutation():
    # Sample Input: abracadabra, 5, k -> abrackdabra
    assert mutate_string("abracadabra", 5, "k") == "abrackdabra"

def test_start_mutation():
    # Testing mutation at the very first index
    assert mutate_string("hello", 0, "j") == "jello"

def test_end_mutation():
    # Testing mutation at the last index
    assert mutate_string("python", 5, "m") == "pythom"