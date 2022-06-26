from Test_cycle.Regression.Regression_cycle import Regression_cycle
from WebDriver import WebDriver


def test_cycle_execution(_driver: WebDriver):
    try:
        for test in Regression_cycle.regression_tests:
            test.execute(_driver)
    except ValueError:
        print(end="")
    finally:
        _driver.driver_close()


driver = WebDriver()
test_cycle_execution(driver)
