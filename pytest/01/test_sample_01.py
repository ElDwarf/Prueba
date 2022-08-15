import pytest

from sample_01 import inc


def test_response_error():
    respuesta = inc(3)
    espectativa = 4
    assert respuesta == espectativa

"""
def test_answer_with_error():
    assert inc(3) != 5
"""
