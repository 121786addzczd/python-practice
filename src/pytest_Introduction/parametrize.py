# translator.pyのGoogleTranslatorを呼び出してテスト
# 実行コマンド「pytest parametrize.py -s -p no:warnings」
from translator import GoogleTranslator
import pytest


input_data = [
    ("私の名前は佐藤です。", "日本語", "英語", "My name is Sato."),
    ("こんにちは", "日本語", "英語", "Hello"),
    ("おはよう", "日本語", "英語", "good morning")
]


@pytest.fixture(scope="module")
def google_translator() -> GoogleTranslator:
    print("Creating GoogleTranslator instance...")
    return GoogleTranslator()


@pytest.mark.parametrize("input_a, input_b, input_c, input_d", input_data)

def test_convert(input_a, input_b, input_c, input_d, google_translator: GoogleTranslator) -> None:
    print(f"input_a:{input_a}")
    print(f"input_b:{input_b}")
    print(f"input_c:{input_c}")
    print(f"input_d:{input_d}")
    text_translated = google_translator.convert(input_a, input_b, input_c)
    assert text_translated == input_d # 翻訳された文章が同じか