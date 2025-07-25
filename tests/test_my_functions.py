import pytest
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(1, 2)
    assert result == 3
    assert my_functions.add(1, 2) == 3
    assert my_functions.add(1, 1) == 2
    assert my_functions.add(1, 0) == 1
    assert my_functions.add(1, -1) == 0
    assert my_functions.add(1, -2) == -1
    assert my_functions.add(1, -3) == -2

def test_add_strings():
    result= my_functions.add("hello", "world")
    assert result == "helloworld"

def test_divide():
    result = my_functions.divide(1, 2)
    assert result == 0.5
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(10, 0) == 0

@pytest.mark.slow
def test_slow():
    assert True

@pytest.mark.skip(reason="Not implemented yet")
def test_skip():
    assert True

@pytest.mark.xfail(reason="Not implemented yet")
def test_xfail():
    assert False

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (1, 1, 2),
    (1, 0, 1),
    (1, -1, 0),
    (1, -2, -1),
    (1, -3, -2),
])
def test_add_parametrized(a, b, expected):
    assert my_functions.add(a, b) == expected



