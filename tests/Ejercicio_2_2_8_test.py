import pytest
from src.Ejercicio_2_2_8 import bucle_numero_piramide

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (10, "1 \n3 1 \n5 3 1 \n7 5 3 1 \n9 7 5 3 1 \n"),
        (7, "1 \n3 1 \n5 3 1 \n7 5 3 1 \n")
    ]
)
def test_bucle_numero_piramide_params(input_n, expected):
    assert bucle_numero_piramide(input_n) == expected