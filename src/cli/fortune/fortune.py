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


class UserProfile:
    def __init__(self, name: str, birthday: date) -> None:
        """
        UserProfile クラスの初期化メソッド。

        Args:
            name (str): ユーザの名前
            birthday (date): ユーザの誕生日
        """
        self.name = name
        self.birthday = birthday


def tell_fortune(user_profile: UserProfile, today: date) -> str:
    """
    与えられた UserProfile オブジェクトと今日の日付に基づいて、運勢の文字列を返す。

    Args:
        user_profile (UserProfile): 運勢を占う対象の UserProfile オブジェクト。
        today (date): 今日の日付。

    Returns:
        str: その人物の運勢を含む文字列。
    """
    lucky_color = random.choice(LUCKY_COLORS)
    lucky_number = random.choice(LUCKY_NUMBERS)

    return FORTUNE_OUTPUT_TEMPLATE.format(
        today=today,
        name=user_profile.name,
        lucky_color=lucky_color,
        lucky_number=lucky_number,
    )


def main() -> None:
    name = "ファルコ"
    birthday = date(2005, 4, 4)
    user_profile = UserProfile(name, birthday)
    today = date.today()

    result = tell_fortune(user_profile, today)
    print(result)


if __name__ == "__main__":
    main()
