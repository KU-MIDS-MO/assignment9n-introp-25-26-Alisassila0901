from vector import *
import pytest

def test_vector1():
    u = Vector(4)
    v = Vector(4)
    u[0] = 1
    u[1] = 2
    u[2] = -3
    u[3] = -4
    v[1] = 5
    v[2] = 7
    assert u*v == -11

def test_vector2():
    u = Vector(4)
    u[0] = 1
    u[1] = 2
    u[2] = -3
    u[3] = -4
    assert [x for x in u*1.5] == [1.5, 3.0, -4.5, -6.0]

def test_vector3():
    u = Vector(4)
    u[0] = 1
    u[1] = 2
    u[2] = -3
    u[3] = -4
    assert [x for x in 1.5*u] == [1.5, 3.0, -4.5, -6.0]

def test_vector4():
    u = Vector(2)
    v = Vector(4)
    with pytest.raises(ValueError) as info:
        u*v
    assert info.value.args[0] == 'dimensions must agree'
