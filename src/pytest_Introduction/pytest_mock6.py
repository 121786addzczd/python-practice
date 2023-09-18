# 例外処理を実行
from translator import GoogleTranslator
import pytest


def test_mock_exception(mocker):
    mock_obj = mocker.patch("translator.GoogleTranslator.get_language_id")
    mock_obj.side_effect = Exception("ConvertException") # 例外を設定

    with pytest.raises(Exception) as e: # 例外objをeとして取得
        trans = GoogleTranslator()
        text_translated = trans.convert("私の名前は佐藤です。", "日本語", "英語")
        print(text_translated)

    # 例外の中身確認
    print(e.value.args[0])

