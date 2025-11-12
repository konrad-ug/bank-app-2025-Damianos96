import pytest

class Calculator:
    def sum(self, a, b):
        return a+b


class TestCalculator:
    @pytest.mark.parametrize("num1, num2, expected", [
        (5, 10, 15),
        (-5, -10, -15),
        (0, 0, 0),
        (5, 0, 5),
        (5, -10, -5)
    ],
    ids=[
        "both positive",
        "both negative",
        "both zero",
        "one zero",
        "mixed signs"
    ])
    def test_sum(self, num1, num2, expected):
        calc=Calculator()
        result = calc.sum(num1, num2)
        assert result == expected