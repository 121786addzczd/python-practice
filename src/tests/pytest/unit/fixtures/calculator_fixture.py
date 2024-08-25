import pytest
from src.calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()
