import pytest
from store import calculate_bill, check_stock, update_stock


def test_calculate_bill():
    assert calculate_bill(30, 2) == 60


def test_sufficient_stock():
    assert check_stock(10, 2) is True


def test_insufficient_stock():
    assert check_stock(3, 5) is False


def test_stock_update():
    assert update_stock(10, 2) == 8


def test_invalid_stock_update():
    with pytest.raises(ValueError, match="Insufficient stock"):
        update_stock(3, 5)
