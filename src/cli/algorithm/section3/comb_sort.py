"""
comb_sort.py

概要:
    コムソート(Comb Sort)を実装したサンプルスクリプトです。
    バブルソートの改良版で、隣接要素だけでなく一定間隔（gap）を空けた要素同士も比較し、
    gap を徐々に縮めながら並び替えます。gap を縮める過程で、データの大きな要素や
    小さな要素が効率よく端に移動し、後半はバブルソートに近い動作になります。

縮小率 (shrink factor):
    - gap は毎回 gap / shrink_factor によって縮めます。
    - この縮小率は経験的に 1.3 前後が最も効率的とされており、Donald Knuth らによる
      実験でも多く採用されています。

計算量 (Big O):
    - 最良計算量 (Best): O(n log n)
    - 平均計算量 (Average): O(n^2 / 2^p) ※ p は比較回数による減速効果の程度
    - 最悪計算量 (Worst): O(n^2)
    - 空間計算量 (Space): O(1)    ※インプレースソート

特徴:
    - バブルソートより高速で、実装が容易
    - gap 縮小率を変えることで性能に影響が出る
    - 大きな要素の移動を早めることができる

使用方法:
    ターミナルやコマンドプロンプトで以下を実行します:
        python comb_sort.py

    必要に応じて、__main__ 部分のリスト生成コードや縮小率の定数を変更して、
    挙動や実行速度の変化を確認してください。
"""

from typing import List
import random

SHRINK_FACTOR = 1.3  # gapの縮小率（経験的に最適とされる値）


def comb_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers
    swapped = True

    while gap != 1 or swapped:
        # gap が 1 でない、または 前回のループで要素の入れ替えがあった場合は継続
        # → gap が 1 かつ swapped が False のときのみ終了
        gap = int(gap / SHRINK_FACTOR)
        if gap < 1:
            gap = 1

        swapped = False

        for i in range(0, len_numbers - gap):
            if numbers[i] > numbers[i + gap]:
                numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
                swapped = True

    return numbers


if __name__ == "__main__":
    # nums = [2, 9, 1, 8, 7, 3, 5]
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(f"ランダムに生成された数字配列:{nums=}")
    print(comb_sort(nums))
