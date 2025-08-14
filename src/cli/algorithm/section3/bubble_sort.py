"""
bubble_sort.py

概要:
    バブルソート(Bubble Sort)を実装したサンプルスクリプトです。
    隣接する要素を比較し、大小関係が逆であれば入れ替える操作を繰り返して
    リストを昇順に並び替えます。

計算量 (Big O):
    - 最良計算量 (Best): O(n)    ※すでにソート済みの場合（最適化ありの場合）
    - 平均計算量 (Average): O(n^2)
    - 最悪計算量 (Worst): O(n^2)
    - 空間計算量 (Space): O(1)    ※インプレースソート

特徴:
    - 実装が容易
    - 要素数が少ない場合や学習用としては有用
    - データ量が多い場合は非効率

使用方法:
    ターミナルやコマンドプロンプトで以下を実行します:
        python bubble_sort.py

    必要に応じて、__main__ 部分のリスト生成コードを変更し、
    データ数や値の範囲を変えて実行結果や速度を比較してください。
"""

from typing import List
import random


def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(f"ランダムに生成された数字配列:{nums=}")
    print(bubble_sort(nums))
