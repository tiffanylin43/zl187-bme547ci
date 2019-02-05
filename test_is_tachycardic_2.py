import pytest


@pytest.mark.parametrize("a, expected", [
    ("  nishiTacHyCARdiC ", bool(1)),
    ("zhegemeiyou", bool(0)),
    ("zhegeyoudiannanTaCHYcarDic", bool(1)),
    ("buzhidaoshuoshenme", bool(0)),
])
def test_is_tachycardic3(a, expected):
    from tachycardia import is_tachycardic
    result = is_tachycardic(a)
    assert result == expected
