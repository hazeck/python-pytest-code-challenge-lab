import pytest
from lib.palindrome import longest_palindromic_substring

# Basic test cases
def test_babad():
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]

def test_cbbd():
    assert longest_palindromic_substring("cbbd") == "bb"

def test_single_char():
    assert longest_palindromic_substring("a") == "a"

def test_two_diff_chars():
    result = longest_palindromic_substring("ac")
    assert result in ["a", "c"]

def test_full_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"

# Edge cases
def test_empty_string():
    assert longest_palindromic_substring("") == ""

def test_no_palindrome():
    # Every character is unique, return any single character
    result = longest_palindromic_substring("abcdefg")
    assert result in list("abcdefg")

def test_all_same_chars():
    assert longest_palindromic_substring("aaaaaa") == "aaaaaa"

def test_palindrome_at_start():
    assert longest_palindromic_substring("abbahello") == "abba"

def test_palindrome_at_end():
    assert longest_palindromic_substring("helloracecar") == "racecar"

def test_multiple_same_length():
    result = longest_palindromic_substring("abcbabcba")
    assert result == "abcbabcba"  # entire string is a palindrome
