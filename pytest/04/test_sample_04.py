import pytest

from sample_04 import inc, inc1, inc2


def test_answer():
    assert inc(3) == 4


def test_answer_with_error():
    assert inc(3) == 5


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        inc1(1, 0)


@pytest.mark.xfail(raises=IndexError)
def test_f():
    inc2([1, 2, 3], 5)


def test_faltate():
    respuesta = inc2([1, 2, 3], 3)
    assert respuesta == 0
