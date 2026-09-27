class verticals:
    def __init__(self,page):
        self.page=page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')

        self.trading=page.locator('(//img[@alt="trading"])[1]')

        self.stockTrading=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.paperTrading=page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.CFD_Trading=page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.development_in_Massachusetts=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.algo_trading_app=page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.custom_trading=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.webportal_trading=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.tradingList=[self.stockTrading,self.paperTrading,self.CFD_Trading,self.development_in_Massachusetts,self.algo_trading_app,self.custom_trading,self.webportal_trading]
            

        self.retail_Ecommerce=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1])')
        self.ecommerceWebsiteDev=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.ecommerceAppDev=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.retailList=[self.ecommerceAppDev,self.ecommerceWebsiteDev]
        


        self.healthCare=page.locator('(//a[@href="https://www.tranktechnologies.com/healthcare-mobile-app-development-company"])[1]')
        self.dietAndNutri=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.healthTrackingApp=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.healthCareList=[self.dietAndNutri,self.healthTrackingApp]
        
        self.fintech=page.locator('(//a[@href="https://www.tranktechnologies.com/fintech-mobile-app-development-company"])[1]')
        self.pos=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
        self.fintechList=[self.fintech,self.pos,self.crypto]


        self.customApp=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/custom-mob.png"]')
        self.desktopApp=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.hrmApp=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.travelApp=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.datingApp=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.customCRM=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.crmDev=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.erpApp=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.eMobile=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.realEstate=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')

        self.custmAppList=[self.customApp, self.desktopApp, self.hrmApp, self.travelApp, self.datingApp, self.customCRM, self.crmDev, self.erpApp, self.eMobile, self.realEstate]

        ##country dropdown
        self.country_dropDown=page.locator('//select[@id="countrySelector"]')
        self.country_dropDown.select_option('India')

        #page.locator('//option[@value="india"]')
        #page.locator('//option[@value="usa"]')
        #page.locator('//option[@value="uae"]')
        
        
    def click_trading_option(self):
        for i in self.tradingList:
            self.vertical.hover()
            self.trading.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_RetailAndEcomm(self):
        for i in self.retailList:
            self.vertical.hover()
            self.retail_Ecommerce.hover()
            i.click(force=True)
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_healthCare(self):
        for i in self.healthCareList:
            self.vertical.hover()
            self.healthCare.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

