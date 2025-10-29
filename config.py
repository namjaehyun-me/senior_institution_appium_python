from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

# Android 설정
ANDROID_CAPS = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "emulator-5554",
    "appPackage": "com.teammapa.seniorcare.patient",
    "appActivity": "com.teammapa.seniorcare.patient.MainActivity"
}

# iOS 설정
IOS_CAPS = {
    "platformName": "iOS",
    "automationName": "XCUITest",
    "deviceName": "iPhone 16",
    "platformVersion": "18.6",
    "app": "/Users/teammapa/Library/Developer/Xcode/DerivedData/Patient-gjartqafygingneqowigafdbutss/Build/Products/Debug-iphonesimulator/Patient.app"
}

APPIUM_SERVER_URL = "http://localhost:4723"
