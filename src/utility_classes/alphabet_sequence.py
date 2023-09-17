class AlphabetSequence:
    """
    アルファベットの連番を生成するクラス
    
    使用例:
    >>> alphabet_seq = AlphabetSequence()
    >>> alphabet_seq.generate(1)
    'A'
    >>> alphabet_seq.generate(28)
    'AB'
    """
    
    def __init__(self):
        self.ALPHA_START_ASCII = 65
        self.ALPHABET_COUNT = 26

    def generate(self, n: int) -> str:
        """
        アルファベットの連番のn番目の項を生成

        Parameters:
        - n (int): 連番の中の位置。正の整数であること

        Returns:
        - str: アルファベットの連番のn番目の項
            例: 1 -> 'A', 26 -> 'Z', 27 -> 'AA' など。

        Examples:
        - この関数は `ZZ` (702番目) までの連番の生成のみをサポート
        """
        # nが正の整数であることを確認
        if not isinstance(n, int) or n <= 0:
            raise ValueError("nは正の整数である必要があります")
        
        # nが702を超える場合、例外を投げる
        if n > 702:
            raise ValueError("このメソッドは `ZZ` (702番目) までの連番の生成のみをサポートしています。AAAは考慮していない")

        result = ""

        while n:
            n, idx = divmod(n - 1, self.ALPHABET_COUNT)
            char = chr(self.ALPHA_START_ASCII + idx)
            result = char + result

        return result

""" 使用例
alphabet_seq = AlphabetSequence()
START_INDEX = 1  # アルファベットの連番が A から開始することを示す
END_INDEX = 100  # 生成したいアルファベットの連番の終了インデックス

# START_INDEX から始めて、アルファベットの連番を END_INDEX - 1 番目まで生成・表示する
for i in range(START_INDEX, END_INDEX):
    print(alphabet_seq.generate(i))
"""