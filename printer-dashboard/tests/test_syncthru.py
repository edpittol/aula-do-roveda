import pytest
from syncthru_mock import get_toner


def test_critical_printer_returns_low_toner():
    level = get_toner("192.168.1.10")
    assert isinstance(level, int)
    assert level <= 10


def test_ok_printer_returns_healthy_toner():
    level = get_toner("192.168.1.11")
    assert isinstance(level, int)
    assert level > 10


def test_inaccessible_printer_returns_none():
    level = get_toner("192.168.1.99")
    assert level is None
