# 様々な関数のテストを表示
def test_calculate() -> None:
    result = 5 * 2
    assert result == 10


def test_len() -> None:
    text = "Hello World!"
    assert len(text) == 12


def test_contain() -> None:
    text = "Hello World"
    assert "rld" in text