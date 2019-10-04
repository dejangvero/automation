import pytest
import unittest2
from pages.home.categories_page import CategoriesPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterTest(unittest2.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.cp = CategoriesPage(self.driver)

    @pytest.mark.run(order=1)
    def test_numberOfPopular(self):
        self.cp.login("dejo991+test01@gmail.com", "Balkon22*")
        self.cp.homePageCattegories()
        result = self.cp.verifyNumberOfPopular()
        assert result == 7

    @pytest.mark.run(order=2)
    def test_numberOfBestSellers(self):
        self.cp.login("dejo991+test01@gmail.com", "Balkon22*")
        self.cp.homePageCattegories()
        self.cp.clickOnBestSeller()
        result = self.cp.verifyNumberOfBestSellers()
        assert result == 7

    @pytest.mark.run(order=3)
    def test_SearchResults(self):
        result = self.cp.exportSearchResults("Printed dresses")
        assert result == 5
















