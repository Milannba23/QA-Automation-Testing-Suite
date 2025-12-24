from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://www.kupujemprodajem.com")
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    # 1. Pretraga
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "keywords")))
    search_box.send_keys("iPhone 15")
    search_box.send_keys(Keys.RETURN)
    print("Pretraga započeta...")

    # 2. Čekamo da se stranica sa rezultatima i filterima potpuno učita
    time.sleep(10) 
    
    # 3. Pronalaženje polja preko ID-ja (ovo je najsigurnija metoda na KP)
    print("Pokušavam da unesem filtere...")
    
    # Koristimo XPath koji cilja tačno polja za cenu
    price_from = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='price-from']")))
    price_to = driver.find_element(By.XPATH, "//input[@data-testid='price-to']")

    price_from.send_keys("500")
    time.sleep(2)
    price_to.send_keys("1000")
    price_to.send_keys(Keys.RETURN)
    
    print("--- USPEH: Filteri su primenjeni! ---")
    time.sleep(10)

except Exception as e:
    print(f"Došlo je do greške: {e}")

finally:
    driver.quit()
