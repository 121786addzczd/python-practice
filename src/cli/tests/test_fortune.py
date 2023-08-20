from datetime import date
import pytest
from fortune.fortune import BirthdayBasedFortuneTeller, UserProfile


@pytest.mark.parametrize(
    "birthday, today, expected",
    [
        (date(1993, 4, 14), date(1993, 4, 14), 777),
        (date(1993, 4, 14), date(1993, 4, 15), 0),
        (date(1993, 4, 14), date(1993, 5, 14), 0),
    ],
)
def test_birthday_based_lucky_number(birthday, today, expected):
    User_profile = UserProfile(name="Bob", birthday=birthday)
    fortune_teller = BirthdayBasedFortuneTeller()

    actual = fortune_teller._lucky_number(User_profile, today)

    assert actual == expected
