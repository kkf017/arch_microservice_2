"""Module to test random_n_chars() function."""

import pytest
from microservice.core.handling_string.handling_string import random_n_chars

# https://pytest-with-eric.com/integrations/pytest-github-actions/

def test_random_n_chars_1():
    """
    Function to check if generated string is correct.
    .test normal
    """
    x = random_n_chars(n=16)
    assert isinstance(x, str)
    assert len(x) == 16


def test_random_n_chars_2():
    """
    Function to check if TypeError is raised when input is string.
    .test error
    """
    with pytest.raises(TypeError):
        random_n_chars(n="abc")

def test_random_n_chars_3():
    """
    Function to check if ...
    .test limit
    """
    x = random_n_chars(n=10**6)
    assert isinstance(x, str)
    assert len(x) == 10**6
