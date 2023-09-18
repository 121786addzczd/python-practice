# translator.pyのGoogleTranslatorを呼び出してテスト
# pytestを実行すると警告がでる場合は以下コマンド実行
# pytest pytest_mock1.py -v -p no:warnings
from translator import GoogleTranslator
import pytest


@pytest.fixture(scope="module")
def google_translator() -> GoogleTranslator:
    print("Creating GoogleTranslator instance...")
    return GoogleTranslator()


def test_japanese_to_english(google_translator: GoogleTranslator, mocker) -> None:
    mocker.patch("translator.GoogleTranslator.convert", return_value = "Hello World!")
    text_translated = google_translator.convert("私の名前は佐藤です。", "日本語", "英語")
    print(text_translated)
    # assert text_translated == "My name is Sato."


def test_english_to_japanese(google_translator: GoogleTranslator, mocker) -> None:
    mocker.patch("translator.GoogleTranslator.get_language_id", return_value = "ja")
    text_translated = google_translator.convert("私の名前は佐藤です。", "日本語", "英語")
    print(text_translated)
    # assert text_translated == "私の名前は佐藤です。"