import pytest
from alphabet_sequence import AlphabetSequence

def test_generate_alphabet_sequence():
    """
    AlphabetSequenceクラスのgenerateメソッドのテストを行う

    このテストは以下のケースをカバーしている
    1. 基本的なテスト
        - 連番の最初のアルファベット（A）の生成
        - 連番の26番目のアルファベット（Z）の生成
        - 2文字のアルファベットの初めての連番（AA）の生成
        - 2文字のアルファベットの最後の連番（ZZ）の生成

    2. 不正な入力値に対するテスト
        - 0や負の整数など、正の整数でない入力に対する例外のテスト

    3. サポートされていない連番の生成に関するテスト
        - 702（ZZ）を超える値の入力に対する例外のテスト

    4. 型エラーのテスト
        - 文字列や浮動小数点数など、整数でない入力に対する例外のテスト
    """
    alphabet_seq = AlphabetSequence()

    # 基本のテスト
    assert alphabet_seq.generate(1) == 'A'
    assert alphabet_seq.generate(26) == 'Z'
    assert alphabet_seq.generate(27) == 'AA'
    assert alphabet_seq.generate(702) == 'ZZ'

    # 不正な値に対するテスト
    with pytest.raises(ValueError, match="nは正の整数である必要があります"):
        alphabet_seq.generate(0)
    with pytest.raises(ValueError, match="nは正の整数である必要があります"):
        alphabet_seq.generate(-1)

    # サポートされていない連番の生成に関するテスト
    with pytest.raises(ValueError, match="このメソッドは `ZZ` \\(702番目\\) までの連番の生成のみをサポートしています。"):
        alphabet_seq.generate(703)

    # 型エラーのテスト
    with pytest.raises(ValueError, match="nは正の整数である必要があります"):
        alphabet_seq.generate('A')
    with pytest.raises(ValueError, match="nは正の整数である必要があります"):
        alphabet_seq.generate(1.5)
