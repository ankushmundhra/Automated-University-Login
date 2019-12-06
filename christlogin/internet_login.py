
def main():
  usernameStr = input("Enter username:")
  passwordStr = input("Enter password:")

  browser = webdriver.Chrome()
  browser.get(('http://192.168.100.100:8090/'))

  # fill in username and hit the next button
  username = browser.find_element_by_id('username')
  username.send_keys(usernameStr)

  nextButton = browser.find_element_by_id('password')
  nextButton.click()

  # wait for transition then continue to fill items

  password = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "password")))
  password.send_keys(passwordStr)

  signInButton = browser.find_element_by_id('loginbutton')
  signInButton.click()
