from plates import is_valid


def test_a():
    assert is_valid("HELLO") == True
    assert is_valid("CS50") == True


def test_b():
    assert is_valid("a") == False
    assert is_valid("a123") == False
    assert is_valid("CS05") == False
    assert is_valid("50") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
