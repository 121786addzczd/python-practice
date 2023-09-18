# 例外処理を実行
from translator import GoogleTranslator
import pytest


def test_convert():
    # 例外が表示された場合でもクリアとする
    with pytest.raises(Exception):
    # with pytest.raises(KeyError): # 個別でも可
        trans = GoogleTranslator()
        trans.convert("私の名前は佐藤です。", "日本語", "ポルトガル語")


