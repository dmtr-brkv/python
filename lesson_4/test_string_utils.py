import pytest
from string_utils import StringUtils

@pytest.mark.parametrize("input_text, expected_output", [
        ("hello", "Hello"),
        ("Hello", "Hello"),
        ("привет", "Привет"),
        ("Negativ", "negativ"),
    ],)
def test_capitalize(input_text, expected_output):
    string_utils = StringUtils()
    res = string_utils.capitalize(expected_output)
    assert res == expected_output

@pytest.mark.parametrize("input_text, expected_output", [
        ("    Hello", "Hello"),
        ("  ", ""),
        ("   Привет", "Привет"),
        ("Negativ", " Negativ"),
    ],)
def test_trim(input_text, expected_output):
    string_utils = StringUtils()
    res = string_utils.trim(expected_output)
    assert res == expected_output

@pytest.mark.parametrize("string, symbol",[
    ("SkyPro", "S"),
    ("SkyPro", "U"),
    ("", "a"),
    ("hello", ""),
    ("abc", "c"),
],)
def test_contains(string, symbol):
    bool = StringUtils()
    return bool

@pytest.mark.parametrize("string, symbol, result", [
        ("Hello", "H", "ello"),
        ("SkyPro", "p", "Skyro"),
        ("Привет","ве", "Прит"),
        ("Nega", "tiv" " Negativ")
    ],)
def delete_symbol(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == result

