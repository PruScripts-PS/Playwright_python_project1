class blog:
    def __init__(self,page):
        self.page=page

        self.blog = page.locator('//a[@href="https://www.tranktechnologies.com/blog/"]')

        self.appDev=page.locator('//a[@href="/blog/category/app-development/"]')
        self.webDev=page.locator('//a[@href="/blog/category/web-development/"]')
        self.softwareDev=page.locator('//a[@href="/blog/category/software-development/"]')
        self.digitalMark=page.locator('//a[@href="/blog/category/digital-marketing/"]')
        self.emailMark=page.locator('//a[@href="/blog/category/email-marketing/"]')
        self.AI=page.locator('//a[@href="/blog/category/artificial-intelligence/"]')
        self.UIUXDesign=page.locator('//a[href="/blog/category/ui-ux-design/"]')

            
