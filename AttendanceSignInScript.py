from selenium import webdriver

driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://njit2.mrooms.net/auth/saml2/login.php?wants")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_id("username").send_keys("ENTER YOUR USER NAME HERE")
driver.find_element_by_id("password").send_keys("ENTER YOUR PASSWORD HERE")
driver.find_element_by_name("_eventId_proceed").click()
driver.find_element_by_link_text("17 F - CS 115001-Intro To Comp Sci I C++").click()
driver.find_element_by_link_text("Attendance").click()
driver.find_element_by_link_text("Submit attendance").click()
driver.find_element_by_id("id_status_6065").click()
driver.find_element_by_name("submitbutton").click()
driver.quit()
