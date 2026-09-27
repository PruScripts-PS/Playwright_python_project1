class technologies:
    def __init__(self, page):
        self.page = page

        self.technologies = page.locator('(//a[text()="Technologies"])[1]')

        self.eCommerce_Development = page.locator('(//img[@alt="ecommerce"])[1]')
        
        self.Magento_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.Opencart_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.Codeigniter_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.WordPress_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.Big_Commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.Shopify_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.CS_Cart_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.Node_JS_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.Nop_Commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.Woo_Commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.Laravel_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.Prestashop_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.Drupal_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.Wix_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.Joomla_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.React_JS_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
        self.Express_JS_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')

        self.eCommerce_links = [self.Magento_Development, self.Opencart_Development, self.Codeigniter_Development, self.WordPress_Development, self.Big_Commerce, self.Shopify_Development, self.CS_Cart_Development, self.Node_JS_Development, self.Nop_Commerce, self.Woo_Commerce, self.Laravel_Development, self.Prestashop_Development, self.Drupal_Development, self.Wix_Development, self.Joomla_Development, self.React_JS_Development, self.Express_JS_Development]

        


        self.Mobile_App_Development = page.locator('(//img[@alt="mobile app"])[1]')

        self.reactive=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.xamarin=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.enterpriceMobile=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.kotline=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.Flutter_Mobile_App_Development = page.locator('(//a[contains(@href,"flutter-mobile-app-development")])[1]')
        self.Ionic_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.Swift_App_Development = page.locator('(//a[contains(@href,"swift-mobile-app-development")])[1]')
        self.Appointment_Booking_Development = page.locator('(//a[contains(@href,"appointment-booking-development")])[1]')

        self.mobile_app_links = [self.reactive, self.xamarin, self.enterpriceMobile, self.kotline, self.Flutter_Mobile_App_Development, self.Ionic_App_Development, self.Swift_App_Development, self.Appointment_Booking_Development]

    

        #Artificial_Intelligence
        self.Artificial_Intelligence = page.locator('(//a[contains(@href,"artificial-intelligence")])[1]')



    def click_eCommerce_links(self):
        for i in self.eCommerce_links:
            self.technologies.hover()
            self.eCommerce_Development.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()



    def click_mobile_app_links(self):
        for i in self.mobile_app_links:
            self.technologies.hover()
            self.Mobile_App_Development.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()


    def click_Artificial_Intelligence(self):
        self.technologies.hover()
        self.Artificial_Intelligence.hover()
        self.page.wait_for_load_state("load")
