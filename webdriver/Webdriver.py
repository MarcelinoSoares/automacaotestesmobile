from appium import webdriver


class Driver:
    def __init__(self):
        desired_cap = {
            "platformName": "Android",
            "avd": "AppiumP",
            "deviceName": "emulator-5554",
            "appPackage": "com.android.calculator2",
            "appActivity": "com.android.calculator2.Calculator"
        }
        self.instance = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
