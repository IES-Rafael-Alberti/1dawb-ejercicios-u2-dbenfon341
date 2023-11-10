import pytest
from src.Ejercicio_2_2_1 import bucle_palabra

@pytest.mark.parametrize(
    "input_n, expected",
    [
        ("manolo", "manolo.manolo.manolo.manolo.manolo.manolo.manolo.manolo.manolo.manolo."),
        ("Martillo", "Martillo.Martillo.Martillo.Martillo.Martillo.Martillo.Martillo.Martillo.Martillo.Martillo.")
    ]
)
def test_bucle_palabra_params(input_n, expected):
    assert bucle_palabra(input_n) == expected