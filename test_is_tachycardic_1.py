def test_is_tachycardic1():
    from tachycardia import is_tachycardic
    result = is_tachycardic("   yhdeTachyCardiC ")
    expected = bool(1)
    assert result == expected


def test_is_tachycardic2():
    from tachycardia import is_tachycardic
    result = is_tachycardic("   hahahahanihaoya ")
    expected = bool(0)
    assert result == expected


