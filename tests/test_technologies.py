




import pytest
from pages.techlogie_page import technologies


@pytest.mark.smoke
def test_ecom(page):
    tech = technologies(page)
    tech.click_eCommerce_links()


@pytest.mark.smoke
def test_mobileApp(page):
    mobileApp = technologies(page)
    mobileApp.click_mobile_app_links()


@pytest.mark.smoke
def test_AI(page):
    AIApp = technologies(page)
    AIApp.click_Artificial_Intelligence()