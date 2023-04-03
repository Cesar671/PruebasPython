import pytest
@pytest.mark.parametrize(
    ["a", "b", "resp"],[
        (2,3,8),
        (5,0,1),
        (5,3,125),
    ]
)
def test_potencia(a, b, resp):
    assert a**b == resp
