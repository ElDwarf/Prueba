import pytest

from sample_02 import  inc

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        inc(1, 0)
