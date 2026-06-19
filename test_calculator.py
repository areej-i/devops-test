from calculator import add, subtract, multiply, divide
def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3      

def test_multiply():
    assert multiply(3, 4) == 12 

def test_divide():
    assert divide(10, 2) == 5
    try:
        divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"