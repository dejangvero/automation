from base.basepage import BasePage
import logging
import utilities.custom_logger as cl

class RegisterPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

    #Locators
    signInButton = "//a[@class='login']"
    emailField = "//input[@id='email_create']"
    createAccountButton = "//i[@class='icon-user left']"
    # genderSelect = "//input[@id='id_gender1']"
    genderCSS = "#id_gender1"
    firstNameField = "//input[@id='customer_firstname']"
    lastNameField = "//input[@id='customer_lastname']"
    passwordField = "//input[@id='passwd']"
    # dobDays = "//select[@id='days']"
    # dobMonth = "//select[@id='months']"
    # dobYear = "//select[@id='years']"
    dobDaysID = "days"
    dobMonthID = "months"
    dobYearsID = "years"
    companyField = "//input[@id='company']"
    address1Field = "//input[@id='address1']"
    cityField = "//input[@id='city']"
    stateField = "//select[@id='id_state']"
    zipField = "//input[@id='postcode']"
    countryField = "//select[@id='id_country']"
    phoneField = "//input[@id='phone_mobile']"
    aliasField = "//input[@id='alias']"
    registerButton = "//button[@id='submitAccount']"
    signOutButton = "//a[@class='logout']"


    def clickSignIn(self):
        self.elementClick(self.signInButton, "xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self.emailField, "xpath")

    def clearEmailField(self):
        clearEmail = self.getElement(self.emailField, "xpath")
        clearEmail.clear()

    def clickOnCreateAccountButton(self):
        self.elementClick(self.createAccountButton, "xpath")

    def selectGender(self):
        self.elementClick(self.genderCSS, "css")

    def enterFirstName(self, firstname):
        self.sendKeys(firstname, self.firstNameField, "xpath")

    def clearFirstname(self):
        clearFirstName = self.getElement(self.firstNameField, "xpath")
        clearFirstName.clear()

    def enterLastName(self, lastname):
        self.sendKeys(lastname, self.lastNameField, "xpath")

    def clearLastName(self):
        clearLastName = self.getElement(self.lastNameField, "xpath")
        clearLastName.clear()

    def enterPassword(self, password):
        self.sendKeys(password, self.passwordField, "xpath")

    def clearPassword(self):
        clearPassword = self.getElement(self.passwordField, "xpath")
        clearPassword.clear()

    def enterDayofBirth(self, days):
        self.selectValueDropdown(days, self.dobDaysID)

    def enterMonthofBirth(self, month):
        self.selectValueDropdown(month, self.dobMonthID)
    def enterYearofBirth(self, year):
        self.selectValueDropdown(year, self.dobYearsID)

    def enterCompany(self, company):
        self.sendKeys(company, self.companyField, "xpath")

    def clearCompany(self):
        clearCompany = self.getElement(self.companyField, "xpath")
        clearCompany.clear()

    def enterAddress(self, address):
        self.sendKeys(address, self.address1Field, "xpath")

    def clearAddress(self):
        clearAddress = self.getElement(self.address1Field, "xpath")
        clearAddress.clear()

    def enterCity(self, city):
        self.sendKeys(city, self.cityField, "xpath")

    def clearCity(self):
        clearCity = self.getElement(self.cityField, "xpath")
        clearCity.clear()

    def selectState(self, state):
        self.selectValueDropdown(state, self.stateField, "xpath")

    def enterZipCode(self, zipcode):
        self.sendKeys(zipcode, self.zipField, "xpath")

    def clearZipCode(self):
        clearZipCode = self.getElement(self.zipField, "xpath")
        clearZipCode.clear()

    def selectCountry(self, country):
        self.selectValueDropdown(country, self.countryField, "xpath")

    def enterPhoneNumber(self, phonenumber):
        self.sendKeys(phonenumber, self.phoneField, "xpath")

    def clearPhoneNumber(self):
        clearPhoneNumber = self.getElement(self.phoneField, "xpath")
        clearPhoneNumber.clear()

    def enterAlias(self, alias):
        self.sendKeys(alias, self.aliasField, "xpath")

    def clearAlias(self):
        clearAlias = self.getElement(self.aliasField, "xpath")
        clearAlias.clear()

    def clickRegister(self):
        self.elementClick(self.registerButton, "xpath")

    def clearRegisterForm(self):
        self.clearEmailField()
        self.clearFirstname()
        self.clearLastName()
        self.clearPassword()
        self.clearCompany()
        self.clearAddress()
        self.clearCity()
        self.clearZipCode()
        self.clearPhoneNumber()
        self.clearAlias()

    def registerUser(self, email="", firstname="", lastname="", password="", days="", month="", year="", company="", address="", city="", state="", zipcode="", country="", phonenumber="", alias=""):
        self.clickSignIn()
        self.enterEmail(email)
        self.clickOnCreateAccountButton()
        self.util.sleep(2)
        self.selectGender()
        self.enterFirstName(firstname)
        self.enterLastName(lastname)
        self.enterPassword(password)
        self.enterDayofBirth(days)
        self.enterMonthofBirth(month)
        self.enterYearofBirth(year)
        self.enterCompany(company)
        self.enterAddress(address)
        self.enterCity(city)
        self.selectState(state)
        self.enterZipCode(zipcode)
        self.selectCountry(country)
        self.enterPhoneNumber(phonenumber)
        self.clearAlias()
        self.enterAlias(alias)
        self.clickRegister()


    def verifySuccesfullRegister(self):
        result = self.isElementPresent(self.signOutButton, "xpath")
        return result
















    #