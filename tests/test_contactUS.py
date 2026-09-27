



import pytest
from pages.contactUs_page import contactUs


@pytest.mark.smoke
def test_FillForm(page):
    form=contactUs(page)
    form.fillForm()

@pytest.mark.smoke
def test_devLinks(page):
    devLinksObj=contactUs(page)
    devLinksObj.click_devLinks()


@pytest.mark.smoke
def test_WebdevLinks(page):
    webDevLinksObj=contactUs(page)
    webDevLinksObj.click_WebDevList()


@pytest.mark.smoke
def test_click_UIUX_design(page):
    UIUX_designObj=contactUs(page)
    UIUX_designObj.click_UIUX_design()

@pytest.mark.smoke
def test_click_graphicLinks(page):
    graphicLinksObj=contactUs(page)
    graphicLinksObj.click_graphicLinks()

@pytest.mark.smoke
def test_socialmediapageclick(page):
    socialMediaObj=contactUs(page)
    socialMediaObj.socialmediapageclick()