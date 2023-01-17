from test_bank.bank import value


def test_a():
    assert value("hello") == 0
    assert value("hello, Bob") == 0


def test_b():
    assert value("how you doing?") == 20
    assert value("how are you?") == 20
    assert value("hi, friend!") == 20


def test_c():
    assert value("what's happening?") == 100
    assert value("what's up!") == 100


def test_d():
    assert value("HELLO") == 0
    assert value("Hey") == 20
    assert value("HI") == 20
