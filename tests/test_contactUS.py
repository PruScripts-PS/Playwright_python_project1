



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

@pytest.mark.P1
def test_newArrowAppDev1(page):
    socialMediaObj=contactUs(page)
    socialMediaObj.arrowLinksAppDev()

@pytest.mark.P1
def test_newArrowAndoroidAppDev2(page):
    socialMediaObj=contactUs(page)
    socialMediaObj.arrow2_andoidApps()

##pytest test_file.py
##pytest -m P1

##pytest test_contactUS.py::TestClass