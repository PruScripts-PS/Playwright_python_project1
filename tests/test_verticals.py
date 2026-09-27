



import pytest
from pages.veritcal import verticals

@pytest.mark.smoke
def test_trading(page):
    trade=verticals(page)
    trade.click_trading_option()

@pytest.mark.smoke
def test_RetailEcom(page):
    retail=verticals(page)
    retail.click_RetailAndEcomm()


@pytest.mark.smoke
def test_healthCare(page):
    retail=verticals(page)
    retail.click_healthCare()