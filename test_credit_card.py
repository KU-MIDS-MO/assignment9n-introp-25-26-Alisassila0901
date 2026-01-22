from credit_card import *
import pytest

def test_credit_card1():
    c = CreditCard("My Name", "My Bank", "012345", 3000)
    c.charge (1000)
    c.make_payment(500)
    assert c.get_balance() == 500

def test_credit_card2():
    c = CreditCard("My Name", "My Bank", "012345", 3000)
    with pytest.raises(ValueError):
        c.charge("funny money")

def test_credit_card3():
    c = CreditCard("My Name", "My Bank", "012345", 3000)
    with pytest.raises(ValueError):
        c.make_payment("funny money")
        
