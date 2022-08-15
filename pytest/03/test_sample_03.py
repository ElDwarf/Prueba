import pytest

from sample_03 import  inc


@pytest.mark.xfail(raises=IndexError)
def test_f():
    inc([1, 2, 3], 5)
