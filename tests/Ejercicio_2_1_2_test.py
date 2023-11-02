import pytest
from src.Ejercicio_2_1_2 import comprobar_pwd

@pytest.mark.parametrize(
    "input_n, expected",
    [
        ("asdasdf", "No has acertado."),
        ("fdsadfasdf", "No has acertado."),
        ("fdsagdsadf", "No has acertado."),
        ("asAdsaF", "No has acertado."),
        ("contraseña", "¡Has acertado la contraseña!")
    ]
)
def test_comprobar_pwd_params(input_n, expected):
    assert comprobar_pwd(input_n) == expected