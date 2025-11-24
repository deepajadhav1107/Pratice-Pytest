from calc import add

def test_add():
    print("Running the test for add() function")
    result = add(2, 3)
    print("Result from add():", result)

    assert result == 5
