from fuel import convert, gauge
import pytest

def main():
    test_a()
    test_b()
    test_c()

def test_a():
    assert convert('50/100') == 50
    assert convert('1/100') == 1
    assert convert('99/100')==99
    assert convert('1/1') == 100
    assert convert('0/10') == 0

def test_b():
    with pytest.raises(ZeroDivisionError):
        convert('2/0')
    with pytest.raises(ValueError):
        convert('cat/1')
    with pytest.raises(ValueError):
         convert('3/2')


def test_c():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(50) == '50%'

if __name__== "__main__":
    main()
