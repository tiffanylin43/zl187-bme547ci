import pytest


@pytest.mark.parametrize("a, expected", [
    ("      zhegeshicuode   ", bool(0)),
    ("TACHYCardic", bool(1)),
    ("duileTaCHYcarDic", bool(1)),
    ("TachyCARDICduileduile", bool(1)),
])
def test_is_tachycardic4(a, expected):
    from tachycardia import is_tachycardic
    result = is_tachycardic(a)
    assert result == expected
