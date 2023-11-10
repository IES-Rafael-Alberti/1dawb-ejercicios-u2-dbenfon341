import pytest
from src.Ejercicio_2_1_4 import numero_par_impar

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (5, "El número es impar."),
        (25, "El número es impar."),
        (46, "El número es par."),
        (31, "El número es impar."),
        (17, "El número es impar."),
        (125, "El número es impar.")
    ]
)
def test_numero_par_impar_params(input_n, expected):
    assert numero_par_impar(input_n) == expected