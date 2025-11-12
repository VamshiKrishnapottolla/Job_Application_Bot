from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def login_indeed(driver, creds):
    driver.get("https://secure.indeed.com/account/login")
    time.sleep(2)
    driver.find_element(By.ID, "login-email-input").send_keys(creds["username"])
    driver.find_element(By.ID, "login-password-input").send_keys(creds["password"])
    driver.find_element(By.ID, "login-submit-button").click()
    time.sleep(3)

def apply_to_job(driver, job_link):
    driver.get(job_link)
    time.sleep(3)
    try:
        apply_button = driver.find_element(By.XPATH, "//button[contains(text(),'Apply Now')]")
        apply_button.click()
        print(f"✅ Applied to {job_link}")
    except Exception as e:
        print(f"Skipped {job_link}: {e}")
