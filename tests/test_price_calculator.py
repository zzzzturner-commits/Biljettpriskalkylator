import pytest
from price_calculator import PriceCalculator

def test_calculate_raises_value_error_for_negative_age() -> None:
    calculator = PriceCalculator()

    with pytest.raises(ValueError):
        calculator.calculate(-1)


@pytest.mark.parametrize(
    ("age", "expected_price"),
    [
        (0, 50),
        (11, 50),
        (12, 50),
        (13, 100),
        (64, 100),
        (65, 80),
        (66, 80)

    ],
)
def test_calculate_at_price_boundary(age: int, expected_price: int) -> None:
    calculator = PriceCalculator()

    actual_price = calculator.calculate(age)

    assert actual_price == expected_price