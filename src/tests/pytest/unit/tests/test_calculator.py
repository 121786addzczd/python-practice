import pytest


def test_add_valid_inputs(calculator):
    """数値と数値または文字列と数値の足し算が正しく計算されること"""
    assert calculator.add(1, 2) == 3, "1 + 2 は 3 であるべきです"
    assert (
        calculator.add("1", 2) == 3
    ), "文字列 '1' と数値 2 の足し算が正しく計算されていません"


def test_add_invalid_inputs(calculator):
    """無効な入力が与えられたときに適切な例外が発生すること"""
    with pytest.raises(
        ValueError, match="無効な入力です: 両方の引数は数値でなければなりません"
    ):
        calculator.add("1", "two")


def test_subtract_valid_inputs(calculator):
    """数値と数値または文字列と数値の引き算が正しく計算されること"""
    assert calculator.subtract(5, 3) == 2, "5 - 3 は 2 であるべきです"
    assert (
        calculator.subtract("5", 3) == 2
    ), "文字列 '5' と数値 3 の引き算が正しく計算されていません"


def test_subtract_invalid_inputs(calculator):
    """無効な入力が与えられたときに適切な例外が発生すること"""
    with pytest.raises(
        ValueError, match="無効な入力です: 両方の引数は数値でなければなりません"
    ):
        calculator.subtract("five", 3)


def test_multiply_valid_inputs(calculator):
    """数値と数値または文字列と数値の掛け算が正しく計算されること"""
    assert calculator.multiply(2, 4) == 8, "2 * 4 は 8 であるべきです"
    assert (
        calculator.multiply("2", 4) == 8
    ), "文字列 '2' と数値 4 の掛け算が正しく計算されていません"


def test_multiply_invalid_inputs(calculator):
    """無効な入力が与えられたときに適切な例外が発生すること"""
    with pytest.raises(
        ValueError, match="無効な入力です: 両方の引数は数値でなければなりません"
    ):
        calculator.multiply("two", 4)


def test_divide_valid_inputs(calculator):
    """数値と数値または文字列と数値の割り算が正しく計算されること"""
    assert calculator.divide(10, 2) == 5, "10 / 2 は 5 であるべきです"
    assert (
        calculator.divide("10", 2) == 5
    ), "文字列 '10' と数値 2 の割り算が正しく計算されていません"


def test_divide_invalid_inputs(calculator):
    """無効な入力が与えられたときに適切な例外が発生すること"""
    with pytest.raises(
        ValueError, match="無効な入力です: 両方の引数は数値でなければなりません"
    ):
        calculator.divide(10, "two")


def test_divide_by_zero(calculator):
    """ゼロで割ろうとした時に適切な例外が発生すること"""
    with pytest.raises(ValueError, match="ゼロで割ることはできません"):
        calculator.divide(10, 0)
