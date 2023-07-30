import random
import sys
from datetime import date
from typing import List, Union

FORTUNE_OUTPUT_TEMPLATE = """
{today} の {name} さんの運勢

ラッキーカラー: {lucky_color}
ラッキーナンバー: {lucky_number}
"""


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


class RandomFortuneTeller:
    def __init__(self, lucky_colors: List[str], lucky_numbers: List[int]) -> None:
        """
        RandomFortuneTeller クラスの初期化メソッド。

        Args:
            lucky_colors (List[str]): 選択肢となるラッキーカラーのリスト
            lucky_numbers (List[int]): 選択肢となるラッキーナンバーのリスト
        """
        self.lucky_colors = lucky_colors
        self.lucky_numbers = lucky_numbers

    def tell(self, user_profile: UserProfile, today: date) -> str:
        """
        与えられた UserProfile オブジェクトと今日の日付に基づいて、運勢の文字列を返す。

        Args:
            user_profile (UserProfile): 運勢を占う対象の UserProfile オブジェクト。
            today (date): 今日の日付。

        Returns:
            str: その人物の運勢を含む文字列。
        """
        lucky_color = random.choice(self.lucky_colors)
        lucky_number = random.choice(self.lucky_numbers)

        return FORTUNE_OUTPUT_TEMPLATE.format(
            today=today,
            name=user_profile.name,
            lucky_color=lucky_color,
            lucky_number=lucky_number,
        )


class BirthdayBaseFortuneTeller:
    def tell(self, user_profile: UserProfile, today: date) -> str:
        """
        誕生日に基づいた運勢を返すメソッド。

        Args:
            user_profile (UserProfile): 運勢を占う対象の UserProfile オブジェクト。
            today (date): 今日の日付。

        Returns:
            str: その人物の運勢を含む文字列。
        """
        if user_profile.birthday.month == today.month:
            lucky_color = "red"
        else:
            lucky_color = "blue"

        if user_profile.birthday == today:  #  TODO:後に修正
            lucky_number = 777
        else:
            lucky_number = 0

        return FORTUNE_OUTPUT_TEMPLATE.format(
            today=today,
            name=user_profile.name,
            lucky_color=lucky_color,
            lucky_number=lucky_number,
        )


def get_fortune_teller(
    fortune_teller_type: str,
) -> Union[RandomFortuneTeller, BirthdayBaseFortuneTeller]:
    """
    fortune_teller_typeによって異なるFortuneTellerオブジェクトを返す。

    Args:
        fortune_teller_type (str): 選択するFortuneTellerのタイプ。

    Returns:
        Union[RandomFortuneTeller, BirthdayBaseFortuneTeller]: FortuneTellerオブジェクト。

    Raises:
        ValueError: 不明なfortune_teller_typeが指定された場合。
    """
    if fortune_teller_type == "random":
        lucky_colors = ["red", "green", "blue"]
        lucky_numbers = [1, 2, 3]
        return RandomFortuneTeller(lucky_colors, lucky_numbers)
    elif fortune_teller_type == "birthday":
        return BirthdayBaseFortuneTeller()
    else:
        raise ValueError(f"不明なfortune_teller_type: {fortune_teller_type}")


def main() -> None:
    if len(sys.argv) >= 2:
        fortune_teller_type = sys.argv[1]
    else:
        fortune_teller_type = "random"

    name = "ファルコ"
    birthday = date(2005, 4, 4)
    user_profile = UserProfile(name, birthday)
    today = date.today()

    fortune_teller = get_fortune_teller(fortune_teller_type)

    result = fortune_teller.tell(user_profile, today)
    print(result)


if __name__ == "__main__":
    main()
