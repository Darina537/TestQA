lesson6_step215.py
input2.click()
time.sleep(2)

input3 = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
input3.click()
time.sleep(2)

button = browser.find_element(By.XPATH, "//button[@type='submit']")
button.click()

# закрываем браузер после всех манипуляций
time.sleep(10)
browser.quit()