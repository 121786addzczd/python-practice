"""
selection_sort.py

概要:
    選択ソート (Selection Sort) を実装したサンプルスクリプトです。
    未ソート部分から最小値（または最大値）を探し、先頭の要素と入れ替える操作を繰り返して
    昇順に並び替えます。

計算量 (Big O):
    - 最良計算量 (Best): O(n^2)
    - 平均計算量 (Average): O(n^2)
    - 最悪計算量 (Worst): O(n^2)
    - 空間計算量 (Space): O(1)  ※インプレースソート

特徴:
    - 実装が容易で安定した動作
    - 要素数が少ない場合や学習用として有用
    - 入れ替え回数は最大で (n-1) 回と少ないが、比較回数は多い
    - 安定ソートではない（同じ値の順序が変わる可能性がある）

使用方法:
    ターミナルやコマンドプロンプトで以下を実行します:
        python selection_sort.py

    必要に応じて、__main__ 部分のリスト生成コードを変更し、
    データ数や値の範囲を変えて挙動や速度を比較してください。
"""

from typing import List
import random


def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_index = i
        for j in range(i + 1, len_numbers):
            if numbers[min_index] > numbers[j]:
                min_index = j

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers


if __name__ == "__main__":
    # nums = [1, 5, 2, 8, 7, 3]
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(f"ランダムに生成された数字配列:{nums=}")
    print(selection_sort(nums))
