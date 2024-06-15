# lib/testing/ipdb_debugging_test.py

import pytest
from lib.ipdb_debugging import plus_two

def test_adds_two():
    result = plus_two(3)
    assert result == 5



