from base.basepage import BasePage
import logging
import utilities.custom_logger as cl

class CategoriesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

    #Locators
    signInButton = "//a[@class='login']"
    emailFieldLogIn = "//input[@id='email']"
    passwordFieldLogIn = "//input[@id='passwd']"
    signInButtonLogIN = "//i[@class='icon-lock left']"
    logoToHomePageButton = "//img[@class='logo img-responsive']"
    # popularCategories = "//ul[@id='homefeatured']/li"
    popularCategoriesCSS = "ul[id='homefeatured'] li"
    bestSellersCategories = "//ul[@id='blockbestsellers']/li"
    bestSellerCategoriesButton = "a.blockbestsellers"

    searchTopField = "//input[@id= 'search_query_top']"
    searchButton = "//button[@name= 'submit_search']"
    productTitleSearched = "//ul[@class='product_list grid row']//a[@class='product-name']"


    def clickSignIn(self):
        self.elementClick(self.signInButton, "xpath")

    def enterEmailSignIN(self, email):
        self.sendKeys(email, self.emailFieldLogIn, "xpath")

    def enterPasswordSignIn(self, password):
        self.sendKeys(password, self.passwordFieldLogIn, "xpath")

    def clickonSignINLogIN(self):
        self.elementClick(self.signInButtonLogIN, "xpath")

    def homePageCattegories(self):
        self.elementClick(self.logoToHomePageButton, "xpath")

    def getPopularCategoriesProducts(self):
        result = self.getElementList(self.popularCategoriesCSS, "css")
        return result

    def clickOnBestSeller(self):
        self.elementClick(self.bestSellerCategoriesButton, "css")

    def getBestSellerCategoriesProducts(self):
        result = self.getElementList(self.bestSellersCategories, "xpath")
        return result

    def login(self, email, password):
        self.clickSignIn()
        self.enterEmailSignIN(email)
        self.enterPasswordSignIn(password)
        self.clickonSignINLogIN()

    def verifyNumberOfPopular(self):
        numberOfPopular= len(self.getPopularCategoriesProducts())
        return numberOfPopular

    def verifyNumberOfBestSellers(self):
        numberofBestSellers= len(self.getBestSellerCategoriesProducts())
        return numberofBestSellers

    def enterSearchProducts(self, data):
        self.sendKeys(data, self.searchTopField, "xpath")

    def clickOnSearchButton(self):
        self.elementClick(self.searchButton, "xpath")

    def getSearchTitles(self):
        result = self.getElementList(self.productTitleSearched, "xpath")
        return result

    def exportSearchResults(self, data):
        self.enterSearchProducts(data)
        self.clickOnSearchButton()
        results = self.getSearchTitles()
        my_file = open("C:\Users\Dejan\PycharmProjects\SymphonyTest\\tests\home\\resulttitles.txt", "w")

        for i in results:
            my_file.write(str(i.text) + "\n")

        my_file.close()

        return len(results)

































