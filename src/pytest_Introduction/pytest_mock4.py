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
    mock_obj = mocker.patch("translator.GoogleTranslator.get_language_id")
    mock_obj.side_effect = param_select

    text_translated = google_translator.convert("私の名前は佐藤です。", "日本語", "英語")
    print(text_translated)

    # 引数の中身を確認したい場合はcall_args_listを使用
    mock_args = mock_obj.call_args_list
    print(mock_args)
    assert mock_args[0][0][0] == "日本語"
    assert mock_args[1][0][0] == "英語"