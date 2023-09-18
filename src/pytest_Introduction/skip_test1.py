# テストのスキップ
# python -m pytest skip_test1.py -vコマンドで確認できます
import pytest

def test_hello():
    print("Hello")


# skip(reason=でテストが省かれる ""の中身は任意の文字列
@pytest.mark.skip(reason="write reason")
def test_goodmorning():
    print("goodmorning")


def test_goodafternonn():
    print("goodafternonn")