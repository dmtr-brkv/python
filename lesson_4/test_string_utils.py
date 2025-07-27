import pytest
from string_utils import StringUtils

@pytest.mark.parametrize("input_text, expected_output", [
        ("hello", "Hello"),
        ("Hello", "Hello"),
        ("привет", "Привет"),
    ])
def test_capitalize(input_text, expected_output):
    string_utils = StringUtils()
    res = string_utils.capitalize(expected_output)
    assert res == expected_output


@pytest.mark.parametrize("input_text", [123, None, "", "123", " "])
def test_capitalize_negative(self, input_text):
    with pytest.raises(ValueError):
        StringUtils().capitalize(input_text)


@pytest.mark.parametrize("input_text, expected_output", [
        ("    Hello", "Hello"),
        ("  ", ""),
        ("   Привет", "Привет"),
    ],)
def test_trim(input_text, expected_output):
    string_utils = StringUtils()
    res = string_utils.trim(expected_output)
    assert res == expected_output


@pytest.mark.parametrize("input_text", [123, None])
def test_trim_negative(self, input_text):
    with pytest.raises(ValueError):
        StringUtils().trim(input_text)


@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "a", False),
    ("hello", "", True),
    ("abc", "c", True),
])
def test_contains(string, symbol, expected):
    bool = StringUtils()
    return bool


@pytest.mark.parametrize("string, symbol, expected", [
    ("Hello", "H", "ello"),
    ("SkyPro", "P", "Skyro"),
    ("Привет", "ве", "Прит"),
])
def test_delete_symbol(string, symbol, expected):
    assert StringUtils().delete_symbol(string, symbol) == expected


@pytest.mark.parametrize("string, symbol", [(123, "a"), (None, "b")])
def test_delete_symbol_negative(self, string, symbol):
    with pytest.raises(ValueError):
        StringUtils().delete_symbol(string, symbol)


