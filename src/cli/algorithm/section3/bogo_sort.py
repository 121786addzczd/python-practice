"""
bogo_srt.py

概要:
    「ボゴソート (Bogo Sort)」を実装したサンプルスクリプトです。
    ボゴソートは、リストが昇順になるまでランダムに並び替えを繰り返す
    非効率なソートアルゴリズムの一例です（平均計算量は非常に大きく、実用性はありません）。

使用方法:
    ターミナルやコマンドプロンプトで以下を実行します:
        python bogo_srt.py

注意:
    - 要素数が多い場合、実行時間が極端に長くなる可能性があります。
    - 実用目的ではなく、アルゴリズム学習やネタコードとして使用してください。
"""

import random
from typing import List


def in_order(numbers: List[int]) -> bool:
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))
    # 上と下のコードは同じ意味
    # for i in range(len(numbers) - 1):
    #     if numbers[i] > numbers[i + 1]:
    #         return False
    # return True


def bogo_sort(numbers: List[int]) -> List[int]:
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers


if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(f"ランダムに生成された数字配列:{nums=}")
    print(bogo_sort(nums))
