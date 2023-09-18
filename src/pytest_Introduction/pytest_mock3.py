# 引数によって返り値を複数パターン用意
# translator.pyのGoogleTranslatorを呼び出してテスト
from translator import GoogleTranslator
import pytest


@pytest.fixture(scope="module")
def google_translator() -> GoogleTranslator:
    print("Creating GoogleTranslator instance...")
    return GoogleTranslator()


def test_japanese_to_english(google_translator: GoogleTranslator, mocker) -> None:
    def param_select(param):
        if param == "日本語":
            return "ja"
        else:
            return "fr"
    mocker.patch("translator.GoogleTranslator.get_language_id", side_effect = param_select)
    text_translated = google_translator.convert("私の名前は佐藤です。", "日本語", "英語")
    print(text_translated)