import pytest
import unittest2
from pages.home.register_page import RegisterPage
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterTest(unittest2.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rp = RegisterPage(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("C:\Users\Deki\PycharmProjects\Automation\\tests\home\\testdata.csv"))
    @unpack
    def test_validRegister(self, email, firstname, lastname, password, days, month, year, company, address, city, state, zipcode, country, phonenumber, alias):
        self.rp.registerUser(email, firstname, lastname, password, days, month, year, company, address, city, state, zipcode, country, phonenumber, alias)
        result = self.rp.verifySuccesfullRegister()
        assert result == True

    










