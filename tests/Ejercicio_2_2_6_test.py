import pytest
from src.Ejercicio_2_2_6 import bucle_asterisco

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (5, "\n*\n**\n***\n****\n*****")
    ]
)
def test_bucle_asterisco_params(input_n, expected):
    assert bucle_asterisco(input_n) == expected