from Engine import Engine
from Validator import Validator
from Dictionary import Dictionary
from Stats import Stats
import pytest


def test_validate():
    """Testing validate function to see if it correctly marks acceptable and incorrect inputs"""
    validator = Validator()
    assert validator.validate("PTAK") == 0
    assert validator.validate("MAMA") == -1
    assert validator.validate("TATA") == -1
    assert validator.validate("WAWA") == -1


def test_check_for_illegal():
    """testing check_for_illegal function to see if it can successfully filter out any strings containing characters
    other than letters """
    validator = Validator()
    output1 = validator.check_for_illegal("PTAK")
    assert isinstance(output1, str)
    output2 = validator.check_for_illegal("PTA#")
    assert output2 is None
    output3 = validator.check_for_illegal("PT1K")
    assert output3 is None


def test_find_shortest():
    """Testing find_shortest function of the Dictionary class to see if it can correctly count the number of letters in
the shortest word in the dictionary"""
    dicti = Dictionary()
    shortest = dicti.find_shortest()
    expected = 3
    assert shortest == expected

def test_find_longest():
    """Testing find_longest function of the Dictionary class to see if it can correctly count the number of letters in
the longest word in the dictionary"""
    dicti = Dictionary()
    shortest = dicti.find_longest()
    expected = 8
    assert shortest == expected

