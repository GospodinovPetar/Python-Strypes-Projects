import pytest

from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice('a', 1)
    checkout.addItemPrice('b', 2)
    return checkout

def test_CanCalculateTotal(checkout):
    checkout.addItemPrice('a', 1)
    checkout.addItem('a')
    assert checkout.calculateTotal() == 1

def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem('a')
    checkout.addItem('b')
    assert checkout.calculateTotal() == 3

def test_addDiscount(checkout):
    checkout.addDiscount('a', 3, 2)

def test_canApplyDiscountRule(checkout):
    checkout.addDiscount('a', 3, 2)
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('a')
    assert checkout.calculateTotal() == 2

def test_ExceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem('c')