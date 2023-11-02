import pytest
from src.Ejercicio_2_1_8 import pedir_punto

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (0.0, "Inaceptable"),
        (0.4, "Aceptable"),
        (100, "Meritorio"),
        (0.8, "Meritorio"),
        (0.3, False),
        (0.6, "Meritorio")
    ]
)
def test_pedir_punto_params(input_n, expected):
    assert pedir_punto(input_n) == expected