from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicijalizacija drajvera (Verzija 4.0.2 koju imaš instaliranu)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # 1. Otvaranje sajta i pretraga
    driver.get("https://www.kupujemprodajem.com")
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    print("Tražim polje za pretragu...")
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "keywords")))
    search_box.send_keys("iPhone 15")
    search_box.send_keys(Keys.RETURN)
    print("Pretraga započeta...")

    # 2. Ključni deo: Čekamo rezultate i skrolujemo do filtera
    print("Čekam 8 sekundi da se učitaju rezultati...")
    time.sleep(8) 
    
    # Skrolujemo 400 piksela nadole da bi polja za cenu postala vidljiva Seleniumu
    driver.execute_script("window.scrollBy(0, 400);")
    print("Skrolovanje izvršeno...")
    time.sleep(2)

    # 3. Pronalaženje polja za cenu sa "Fallback" (rezervnom) logikom
    print("Pokušavam da unesem filtere za cenu...")
    
    try:
        # Prvi pokušaj: Preko imena atributa (NAME)
        price_from = wait.until(EC.element_to_be_clickable((By.NAME, "price_from")))
        price_to = driver.find_element(By.NAME, "price_to")
        
        # Aktivacija polja klikom pre kucanja
        price_from.click()
        price_from.send_keys("500")
        print("Uneta minimalna cena (NAME metoda)...")
        
        time.sleep(1)
        
        price_to.click()
        price_to.send_keys("1000")
        print("Uneta maksimalna cena (NAME metoda)...")
        
    except:
        # Drugi pokušaj (rezervni): Preko placeholder-a ako NAME ne radi
        print("NAME metoda nije uspela, pokušavam preko placeholder-a...")
        price_from = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='od']")))
        price_to = driver.find_element(By.XPATH, "//input[@placeholder='do']")
        
        price_from.click()
        price_from.send_keys("500")
        time.sleep(1)
        price_to.click()
        price_to.send_keys("1000")
        print("Cene unete preko placeholder-a.")

    # Slanje filtera
    price_to.send_keys(Keys.RETURN)
    print("--- USPEH: Filteri su primenjeni! ---")
    
    # Pauza od 10 sekundi da sve lepo snimiš
    time.sleep(10)

except Exception as e:
    print(f"Došlo je do greške: {e}")

finally:
    driver.quit()
