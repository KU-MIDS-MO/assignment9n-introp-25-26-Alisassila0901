from vector import *
import pytest

def test_cross1():
    u = Vector(3)
    v = Vector(3)
    w = Vector(3)
    u[0] = 3
    u[1] = -3
    u[2] = 1
    v[0] = 4
    v[1] = 9
    v[2] = 2
    w[0] = -15
    w[1] = -2
    w[2] = 39
    assert u.cross(v) == w

def test_cross2():
    u = Vector(3)
    v = Vector(3)
    w = Vector(3)
    u[0] = 3
    u[1] = -3
    u[2] = 1
    v[0] = 4
    v[1] = 9
    v[2] = 2
    w[0] = -15
    w[1] = -2
    w[2] = 39
    assert cross(u,v) == w

def test_vector4():
    u = Vector(3)
    v = Vector(4)
    with pytest.raises(ValueError):
        u.cross(v)
