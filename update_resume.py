from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s=Service(r"C:\Users\singh\Desktop\Python-selenium\ChromeDriver.exe")
driver = webdriver.Chrome(service=s)

email = input("Enter your naukri email id: ")
password = input("Enter your naukri password: ")
driver.get("https://www.naukri.com/mnjuser/profile?id=&orgn=homepage")
driver.maximize_window()


driver.find_element(By.ID,"usernameField").send_keys(email)
driver.find_element(By.ID,"passwordField").send_keys(password)


driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div/div/div/div/div/div[2]/div/form/div[2]/div[3]/div/button[1]").click()


resumeHeadlineSpans = driver.find_elements(By.CSS_SELECTOR ,"resumeHeadline")
print("resumeHeadlineSpans:  ",resumeHeadlineSpans)
#.find_elements(By.TAG_NAME,"span")

for span in resumeHeadlineSpans:
    if span.text == "Edit":
        span.click()
        break

# Here updating Naukri Profile Resume Headline.
headline = "Engineer (Software Trainee) with 6 months experience in Python Automation Scripting & Sotware Testing."

resumeHeadlineTextArea = driver.find_element(By.CLASS_NAME,"resumeHeadlineTxt")
resumeHeadlineTextArea.clear()
resumeHeadlineTextArea.send_keys(headline)

btnList = driver.find_elements(By.TAG_NAME,"button")

for item in btnList:
    if item.text == "SAVE":
        item.click()
        break

driver.__exit__()

