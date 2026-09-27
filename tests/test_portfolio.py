




import pytest
from pages.portfolio_page import portfolio


@pytest.mark.smoke
def test_portfolioViewMore(page):
    viewMore=portfolio(page)
    viewMore.click_portFolioViewMore()

