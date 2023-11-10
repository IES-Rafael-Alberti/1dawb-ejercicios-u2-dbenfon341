import pytest
from src.Ejercicio_2_2_7 import bucle_multiplicacion

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (5, "5\n10\n15\n20\n25\n30\n35\n40\n45\n50")
    ]
)
def test_bucle_multiplicacion_params(input_n, expected):
    assert bucle_multiplicacion(input_n) == expected