import json
import random
import sys
from datetime import date
from typing import List, Union
from abc import ABC, abstractmethod
from pydantic import BaseModel

FORTUNE_OUTPUT_TEMPLATE = """
{today} の {name} さんの運勢

ラッキーカラー: {lucky_color}
ラッキーナンバー: {lucky_number}
"""


class UserProfile(BaseModel):
    name: str
    birthday: date


class FortuneTeller(ABC):
    def tell(self, user_profile: UserProfile, today: date) -> str:
        """
        ユーザの運勢を伝えるメソッド。
        各子クラスでは、ラッキーカラーとラッキーナンバーをどのように決定するかを実装する。

        Args:
            user_profile (UserProfile): ユーザのプロフィール情報。
            today (date): 今日の日付。

        Returns:
            str: 運勢の結果を含む文字列。
        """
        lucky_color = self._lucky_color(user_profile, today)
        lucky_number = self._lucky_number(user_profile, today)

        return FORTUNE_OUTPUT_TEMPLATE.format(
            today=today,
            name=user_profile.name,
            lucky_color=lucky_color,
            lucky_number=lucky_number,
        )

    @abstractmethod
    def _lucky_color(self, user_profile: UserProfile, today: date) -> str:
        """
        ユーザのラッキーカラーを決定するメソッド。
        各子クラスで実装する。

        Args:
            user_profile (UserProfile): ユーザのプロフィール情報。
            today (date): 今日の日付。

        Returns:
            str: ラッキーカラーの名前。
        """
        pass

    @abstractmethod
    def _lucky_number(self, user_profile: UserProfile, today: date) -> int:
        """
        ユーザのラッキーナンバーを決定するメソッド。
        各子クラスで実装する。

        Args:
            user_profile (UserProfile): ユーザのプロフィール情報。
            today (date): 今日の日付。

        Returns:
            int: ラッキーナンバー。
        """
        pass


class RandomFortuneTeller(FortuneTeller):
    def __init__(self, lucky_colors: List[str], lucky_numbers: List[int]) -> None:
        """
        RandomFortuneTeller クラスの初期化メソッド。

        Args:
            lucky_colors (List[str]): ラッキーカラーのリスト。
            lucky_numbers (List[int]): ラッキーナンバーのリスト。
        """
        self.lucky_colors = lucky_colors
        self.lucky_numbers = lucky_numbers

    def _lucky_color(self, user_profile: UserProfile, today: date) -> str:
        """
        ユーザのラッキーカラーをランダムに決定する。

        Args:
            user_profile (UserProfile): ユーザのプロフィール情報。
            today (date): 今日の日付。

        Returns:
            str: ラッキーカラーの名前。
        """
        return random.choice(self.lucky_colors)

    def _lucky_number(self, user_profile: UserProfile, today: date) -> int:
        """
        ユーザのラッキーナンバーをランダムに決定する。

        Args:
            user_profile (UserProfile): ユーザのプロフィール情報。
            today (date): 今日の日付。

        Returns:
            int: ラッキーナンバー。
        """
        return random.choice(self.lucky_numbers)


class BirthdayBaseFortuneTeller(FortuneTeller):
    def _lucky_color(self, user_profile: UserProfile, today: date) -> str:
        """
        ユーザの誕生日が今月であればラッキーカラーは赤、それ以外は青。

        Args:
            user_profile (UserProfile): ユーザのプロフィール情報。
            today (date): 今日の日付。

        Returns:
            str: ラッキーカラーの名前。
        """
        if user_profile.birthday.month == today.month:
            return "red"
        else:
            return "blue"

    def _lucky_number(self, user_profile: UserProfile, today: date) -> int:
        """
        ユーザの誕生日が今日であればラッキーナンバーは777、それ以外は0。

        Args:
            user_profile (UserProfile): ユーザのプロフィール情報。
            today (date): 今日の日付。

        Returns:
            int: ラッキーナンバー。
        """
        if user_profile.birthday == today:  # TODO:後に修正
            return 777
        else:
            return 0


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
    """
    メインの処理。
    コマンドライン引数またはデフォルトの設定で運勢を占う。
    """
    if len(sys.argv) >= 2:
        fortune_teller_type = sys.argv[1]
    else:
        fortune_teller_type = "random"

    with open("profile.json") as f:
        profile_data = json.load(f)

    user_profile = UserProfile.model_validate(profile_data)

    today = date.today()

    fortune_teller = get_fortune_teller(fortune_teller_type)

    result = fortune_teller.tell(user_profile, today)
    print(result)


if __name__ == "__main__":
    main()
