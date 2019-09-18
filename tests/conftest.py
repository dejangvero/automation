import pytest
from selenium import webdriver
from pages.home.register_page import RegisterPage

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="function")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    if browser == 'firefox':
        baseURL = "http://automationpractice.com/index.php"
        driver = webdriver.Firefox(executable_path="C:\Python27\geckodriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseURL)
        print("Running tests on FF")
    else:
        baseURL = "http://automationpractice.com/index.php"
        driver = webdriver.Chrome(executable_path="C:\Python27\chromedriver.exe")
        driver.get(baseURL)
        print("Running tests on chrome")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")