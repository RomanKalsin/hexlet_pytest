from hexlet_pytest.my_slice import my_slice


def test_slice():
    assert my_slice([1, 2, 3, 4, 5, 6], 1, 4) == [2, 3, 4] 
    assert my_slice([], 1) == []
    assert my_slice([1, 2, 3, 4, 5, 6], -1, 4) == []
    assert my_slice([1, 2, 3, 4, 5, 6], -10) ==  [1, 2, 3, 4, 5, 6]