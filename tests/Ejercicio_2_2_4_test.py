import pytest
from src.Ejercicio_2_2_4 import bucle_numero

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (10, "10,9,8,7,6,5,4,3,2,1,0,"),
        (5, "5,4,3,2,1,0,")
    ]
)
def test_bucle_numero_params(input_n, expected):
    assert bucle_numero(input_n) == expected