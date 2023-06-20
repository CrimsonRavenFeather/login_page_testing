# 2. Write all the above 5 Test scripts in a single class using TestNG annotations
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time


# TESTING OF LOGIN PAGE 

class Registration_test(unittest.TestCase):
    def setUp(self):
        path = "chrome driver\\chromedriver.exe"
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://magnus.jalatechnologies.com/")
    
    def tearDown(self):
        # time.sleep(1)
        self.driver.quit()

    # login with correct details

    def test_1(self):
        login_uname=self.driver.find_element(By.ID,"UserName")
        login_password=self.driver.find_element(By.ID,"Password")
        login_btn=self.driver.find_element(By.ID,"btnLogin")

        login_uname.send_keys("training@jalaacademy.com")
        login_password.send_keys("jobprogram")
        login_btn.submit()

    # login with incorrect details

    def test_2(self):
        login_uname=self.driver.find_element(By.ID,"UserName")
        login_password=self.driver.find_element(By.ID,"Password")
        login_btn=self.driver.find_element(By.ID,"btnLogin")

        login_uname.send_keys("incorrect")
        login_password.send_keys("incorrect")
        login_btn.submit()

    # login with empty fields

    def test_3(self):
        login_btn=self.driver.find_element(By.ID,"btnLogin")
        login_btn.submit()

    # check remember me checkbox 

    def test_4(self):
        login_remember=self.driver.find_element(By.ID,"RememberMe")
        login_remember.click()
    
    # click forgot password

    def test_5(self):
        forgot_pass=self.driver.find_element(By.LINK_TEXT,"Forgot Password")
        forgot_pass.click()

# TESTING FOR FORGOT PASSWORD PAGE :

class test_forgot_password_page(unittest.TestCase):
    def setUp(self):
        path = "chrome driver\\chromedriver.exe"
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://magnus.jalatechnologies.com/")
        forgot_pass=self.driver.find_element(By.LINK_TEXT,"Forgot Password")
        forgot_pass.click()
    
    def tearDown(self):
        # time.sleep(1)
        self.driver.quit()
    
    # Testing to get login details in the email by passing email

    def test_1(self):
        enter_email=self.driver.find_element(By.XPATH,'''//*[@id="Email"]''')
        enter_email.send_keys("sample_email123@gmail.com")
        get_password=self.driver.find_element(By.XPATH,'''//*[@id="btnForgotPassword"]''')
        get_password.click()
    
    # Testing to get login details without passing email

    def test2(self):
        get_password=self.driver.find_element(By.XPATH,'''//*[@id="btnForgotPassword"]''')
        get_password.click()

    # Testing to go back to login page

    def test3(self):
        get_back=self.driver.find_element(By.XPATH,'''//*[@id="frmForgotPassword"]/div[2]/div[1]/a''')
        get_back.click()
        self.driver.get("https://magnus.jalatechnologies.com/")
    



def test_suite():
    test=unittest.TestSuite()
    
    # reg_test=unittest.TestLoader().loadTestsFromTestCase(Registration_test)
    # test.addTests(reg_test)

    fog_pword=unittest.TestLoader().loadTestsFromTestCase(test_forgot_password_page)
    test.addTests(fog_pword)

    return test

if __name__ == "__main__":
    suite=test_suite()
    unittest.TextTestRunner().run(suite)
    
