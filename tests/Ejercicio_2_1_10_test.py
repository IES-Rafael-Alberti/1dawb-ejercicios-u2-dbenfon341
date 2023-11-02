import pytest
from src.Ejercicio_2_1_10 import tipo_de_pizza, pizza_veg, pizza_no_veg

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (1, True),
        (2, False),
    ]
)
def test_tipo_de_pizza_params(input_n, expected):
    assert tipo_de_pizza(input_n) == expected