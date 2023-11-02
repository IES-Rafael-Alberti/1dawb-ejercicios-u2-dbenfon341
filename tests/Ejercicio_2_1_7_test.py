import pytest
from src.Ejercicio_2_1_7 import tipo_de_renta

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (9000, "5"),
        (12000, "15"),
        (22000, "20"),
        (36000, "30"),
        (70545, "45"),
        (37000, "30")
    ]
)
def test_tipo_de_renta_params(input_n, expected):
    assert tipo_de_renta(input_n) == expected