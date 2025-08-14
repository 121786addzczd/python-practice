"""
cocktail_sort.py

概要:
    カクテルソート (Cocktail Sort) を実装したサンプルスクリプトです。
    バブルソートの改良版で、左右両方向に交互に要素を比較・交換しながら
    ソートを行います。これにより、データの一部がソート済みの場合に
    無駄な比較を減らすことができます。

計算量 (Big O):
    - 最良計算量 (Best): O(n)    ※すでにソート済みの場合
    - 平均計算量 (Average): O(n^2)
    - 最悪計算量 (Worst): O(n^2)
    - 空間計算量 (Space): O(1)    ※インプレースソート

特徴:
    - バブルソートに比べて効率が良い場合がある
    - 左右両方向に走査するため、データの偏りに強い
    - 実装はやや複雑だが理解しやすい

使用方法:
    ターミナルやコマンドプロンプトで以下を実行します:
        python cocktail_sort.py

    必要に応じて、__main__ 部分のリスト生成コードを変更し、
    データ数や値の範囲を変えて挙動や速度を比較してください。
"""

from typing import List
import random


# bubble sortの改良版
def cocktail_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1
    while swapped:
        swapped = False

        # 右方向（先頭→末尾方向）に走査して、大きい値を右端へ送る
        for i in range(start, end):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        # 右方向で一度も入れ替えがなければ、すでに全体がソート済みなので終了
        if not swapped:
            break

        swapped = False
        end -= 1  # 末尾側はソート済み領域なので比較範囲を縮める

        # 左方向（末尾→先頭方向）に走査して、小さい値を左端へ送る
        for i in range(end - 1, start - 1, -1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        start += 1  # 先頭側もソート済み領域なので比較範囲を縮める

    return numbers


if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(f"ランダムに生成された数字配列:{nums=}")
    print(cocktail_sort(nums))
