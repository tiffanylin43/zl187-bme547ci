import pytest


@pytest.mark.parametrize("a, expected", [
    ("      tachycrdic   ", bool(1)),
    ("      TachYcrDic   ", bool(1)),
    ("tachycard1c", bool(1)),
    ("   tacHycaRd1c   ", bool(1)),
    ("   TAChycazheshicuode", bool(0)),
    ("TachyARD", bool(0)),
])
def test_is_tachycardic4(a, expected):
    from tachycardia1 import is_tachycardic
    result = is_tachycardic(a)
    assert result == expected
