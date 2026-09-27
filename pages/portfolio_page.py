class portfolio:
    def __init__(self,page):
        self.page=page
        self.portFolio=page.locator('//a[@href="https://www.tranktechnologies.com/portfolio"]')

        

        self.ICSHomeWork=page.locator('//a[@href="https://www.icshomework.in/"]')
        self.wingsPharma=page.locator('//a[@href="https://www.wingspharma.com/"]')
        self.arinaAnimation=page.locator('//a[@href="https://arenasonipat.com/"]')
        self.home360=page.locator('//a[@href="https://home360stores.com/"]')
        #clubMeetings=page.locator('//a[@href=]')
        self.cordsCables=page.locator('//a[@href="https://cordscable.tranktechnologies.com/"]')

        self.portFolioList=[self.ICSHomeWork,self.wingsPharma,self.arinaAnimation,self.home360,self.cordsCables]

    def click_portFolioViewMore(self):
        for i in self.portFolioList:
            self.portFolio.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()