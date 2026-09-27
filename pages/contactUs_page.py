class contactUs:
    def __init__(self,page):
        self.page=page
            

        self.contactUs=page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        self.contactUs.click()
        
    
        ###form
        self.name=page.locator('(//input[@placeholder="Your Name"])[2]')
        self.email=page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.send_otp = page.locator('(//button[contains(text(),"Send OTP")])[2]')
        self.otp = page.locator('(//input[@placeholder="Enter OTP"])[2]')
        self.service=page.locator('(//select[@name="service"])[2]')
        self.company = page.locator('(//input[@placeholder="Your Company"])[2]')
        self.phone = page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.message = page.locator('(//textarea[@placeholder="Message"])[2]')
        self.submit =page.locator('(//input[@value="Submit"])[2]')
        self.page.wait_for_timeout(5000)


        ### Web Development
        self.web_development = page.locator('(//a[@href="https://www.tranktechnologies.com/web-development-company"])[1]')
        self.cms_website = page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        self.custom_web_portal = page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')

        self.WebDevList=[self.web_development,self.cms_website,self.custom_web_portal]
        # for i in self.WebDevList:
        #     i.click()
        #     page.wait_for_load_state("load")
        #     page.go_back()
        # dropDown_eWeb=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]').click()
        # eCommerce_web = page.locator('(//a[@href="https://www.tranktechnologies.com/website-development-company"])[1]').click()
        #page.wait_for_timeout(5000) 
           

    ### UI UX Design

        #UI_UX_Design = page.locator('//a[@href="/ui-ux-design-company"]')
        self.Mobile_App_Design = page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.Responsive_Web_Design = page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        self.Brand_Identity_Design = page.locator('//a[contains(@href,"brand-identity-design")]')
        self.UI_UX_Design=[self.Mobile_App_Design,self.Responsive_Web_Design,self.Brand_Identity_Design]
        # for i in self.UI_UX_Design:
        #     i.click()
        #     page.wait_for_load_state("load")
        #     page.go_back()
        # page.wait_for_timeout(7000)


    ### App Development

        self.iOS = page.locator('//a[contains(@href,"ios-mobile-app-development")]')
        self.Android = page.locator('//a[contains(@href,"android-app-development")]')
        self.Hybrid = page.locator('//a[contains(@href,"hybrid-mobile-app-development")]')
        self.Cross_Platform = page.locator('//a[contains(@href,"cross-platform-mobile-app-development")]')
        self.PWA = page.locator('//a[contains(@href,"progressive-web-app-development")]')
        self.app_development_links = [self.iOS, self.Hybrid,self.Cross_Platform, self.PWA]
        # for i in self.app_development_links:
        #     i.click()
        #     page.wait_for_load_state("load")
        #     page.go_back()
        # page.wait_for_timeout(5000)


    ### Graphic Design

        self.Graphic_Design = page.locator('//a[contains(@href,"graphic-design")]')
        self.Logo_Design = page.locator('//a[contains(@href,"logo-design")]')
        self.Banner_Design = page.locator('//a[contains(@href,"banner-design")]')
        self.Packaging_Design = page.locator('//a[contains(@href,"packaging-design")]')
        self.Business_Cards_Design = page.locator('//a[contains(@href,"business-cards-design")]')
        self.graphic_design_links = [self.Graphic_Design, self.Logo_Design, self.Banner_Design, self.Packaging_Design, self.Business_Cards_Design]
        # for i in self.graphic_design_links:
        #     i.click()
        #     page.wait_for_load_state("load")
        #     page.go_back()
        # page.wait_for_timeout(5000)


        # ### Follow Us

        self.Facebook = page.locator('//a[@href="https://www.facebook.com/TrankTechnologies"]')
        self.LinkedIn = page.locator('//a[@href="https://in.linkedin.com/company/trank-technologies-official"]')
        self.Instagram = page.locator('//a[@href="https://www.instagram.com/tranktechnologies/"]')
        self.Pintrest = page.locator('//[@href="https://in.pinterest.com/tranktechnologies12/"]')
        self.Twitter = page.locator('//a[@href="https://twitter.com/tranktechno"]')
        self.YouTube = page.locator('//a[@href="https://www.youtube.com/channel/UCWu1Y-tfrXf-Utpaft830Cg"]')
        self.Quora = page.locator('//a[@href="https://www.quora.com/profile/Trank-Technologies-1"]')

        self.follow_us_links = [self.Facebook, self.Instagram, self.LinkedIn, self.Twitter, self.YouTube, self.Quora]
    
        page.wait_for_timeout(5000)



        self.eccDevArrow1=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]')
        self.websiteDev=page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company"]')

        self.Android_arrow2=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[2]')
        self.androidAppDev=page.locator('//a[@href="https://www.tranktechnologies.com/android-app-development-company"]')
        self.addDev=page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')

        self.andoidAppLinks=[self.androidAppDev,self.addDev]



    def fillForm(self):
        self.name.fill("Prutha V")
        self.page.wait_for_timeout(5000)
        self.email.fill("prutha.v@gmail.com")
        self.send_otp.click()
        self.otp.fill("5678")
        self.service.select_option("Web Development")
        self.company.fill("Prutha pvt Ltd")
        self.phone.fill("1789065000")
        self.message.fill("Kindly give me required details")
        self.submit.click()
         
    def click_WebDevList(self):
        for i in self.WebDevList:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_UIUX_design(self):
        for i in self.UI_UX_Design:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
        self.page.wait_for_timeout(5000)

    def click_devLinks(self):
        for i in self.app_development_links:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
        self.page.wait_for_timeout(5000)

    def click_graphicLinks(self):
        for i in self.graphic_design_links:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
        self.page.wait_for_timeout(5000)


    def socialmediapageclick(self):
        self.page.wait_for_load_state(state="load")
        self.follow_us_links = [self.Facebook, self.Instagram, self.LinkedIn, self.Twitter, self.YouTube, self.Quora]        
        for i in self.follow_us_links:
            with self.page.context.expect_page() as new_page_info:
                i.click()
            new_tab = new_page_info.value
            new_tab.wait_for_load_state("load")
            new_tab.close()


    def arrowLinksAppDev(self):
        self.eccDevArrow1.click()
        #self.self.websiteDev.click()
        with self.page.context.expect_page() as new_page_info:
            self.websiteDev.click()
        new_tab=new_page_info.value
        new_tab.wait_for_load_state("load")
        new_tab.close()

    def arrow2_andoidApps(self):
        self.Android_arrow2.click()
        for i in self.andoidAppLinks:
            with self.page.context.expect_page() as new_page_info:
                 i.click()
            new_tab=new_page_info.value
            new_tab.wait_for_load_state("load")
            new_tab.close() 
