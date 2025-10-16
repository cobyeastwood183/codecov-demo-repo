from src.calculator import add, subtract

# This is a test for the add function
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# This is a test for the subtract function
def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 1) == -1
