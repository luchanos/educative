import pytest

from workshops.decorators.homeworks.block_1.hw_1 import str_mul


@pytest.mark.parametrize("text, multiplier, expected_text", [
    ("a", 3, "aAa"),
    ("test", 1, "test"),
    ("", 0, None),
    ("testText", 4, "testTextTESTTEXTtestTextTESTTEXT"),
])
def test_str_mul(text, multiplier, expected_text):
    assert str_mul(some_string=text, multiplier=multiplier) == expected_text
