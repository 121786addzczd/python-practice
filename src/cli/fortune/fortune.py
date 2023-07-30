import random
from datetime import date
from typing import Tuple

FORTUNE_OUTPUT_TEMPLATE = """
{today} の {name} さんの運勢

ラッキーカラー: {lucky_color}
ラッキーナンバー: {lucky_number}
"""

LUCKY_COLORS = ["red", "green", "blue"]
LUCKY_NUMBERS = [1, 2, 3]


def tell_fortune(name: str, birthday: date, today: date) -> str:
    """
    与えられた名前、誕生日、今日の日付に基づいて、運勢の文字列を返す

    Args:
        name (str): 運勢を占う対象の人物の名前
        birthday (date): その人物の誕生日
        today (date): 今日の日付

    Returns:
        str: その人物の運勢を含む文字列
    """
    lucky_color = random.choice(LUCKY_COLORS)
    lucky_number = random.choice(LUCKY_NUMBERS)

    return FORTUNE_OUTPUT_TEMPLATE.format(
        today=today,
        name=name,
        lucky_color=lucky_color,
        lucky_number=lucky_number,
    )


def main():
    name = "ファルコ"
    birthday = date(2005, 4, 4)
    today = date.today()

    result = tell_fortune(name, birthday, today)
    print(result)


if __name__ == "__main__":
    main()
