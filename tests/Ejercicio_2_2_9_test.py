import pytest
from src.Ejercicio_2_2_9 import comprobar_pwd

@pytest.mark.parametrize(
    "input_n, expected",
    [
        ("contraseña", "¡Has acertado!")
    ]
)
def test_comprobar_pwd_params(input_n, expected):
    assert comprobar_pwd(input_n) == expected