import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

load_dotenv()

USERNAME = os.getenv('SESSION_USERNAME')
PASSWORD = os.getenv('SESSION_PASSWORD')
LOGIN_URL = os.getenv('LOGIN_URL')
KEEPALIVE_INTERVAL = int(os.getenv('KEEPALIVE_INTERVAL', 10))

USERNAME_SELECTOR = '#LogInViewModel_Email'
PASSWORD_SELECTOR = '#LogInViewModel_Password'
SUBMIT_SELECTOR = '#submitBtn'
OTP_INPUTS_SELECTOR = '.signup-otp'
POST_LOGIN_SELECTOR = 'a[href="/profile/dashboard"]'

print(f"🚀 NUSUK HYBRIDE - {USERNAME} (Selenium Manager AUTO)")

def create_driver():
    """AUTO ChromeDriver - zéro config!"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    # ✅ Selenium Manager AUTO (Selenium 4.6+)
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.implicitly_wait(15)
    return driver

# [login_nusuk_hybrid + keep_session_alive_robust + main = identique précédent]


def login_nusuk_hybrid(driver):
    """MANUAL CF + AUTO reste (OTP auto-submit)"""
    print("\n🌐 LOGIN hajj.nusuk.sa")
    driver.get(LOGIN_URL)
    time.sleep(6)
    
    print("""
    🖱️ MANUAL: COCHE Cloudflare → ATTENDS "Succès!" VERT → ENTRÉE
    """)
    input("⏸️ Entrée après Succès...")
    
    wait = WebDriverWait(driver, 45)
    
    # LOGIN/PASS
    username = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, USERNAME_SELECTOR)))
    password = driver.find_element(By.CSS_SELECTOR, PASSWORD_SELECTOR)
    username.clear(); username.send_keys(USERNAME)
    password.clear(); password.send_keys(PASSWORD)
    
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, SUBMIT_SELECTOR)))
    submit.click()
    print("✅ LOGIN!")
    
    time.sleep(6)
    
    # OTP (remplissage SEUL - auto-submit Nusuk)
    print("📱 OTP")
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, OTP_INPUTS_SELECTOR)))
    
    otp_fields = driver.find_elements(By.CSS_SELECTOR, OTP_INPUTS_SELECTOR)
    if len(otp_fields) != 6:
        print(f"❌ {len(otp_fields)} champs (attendu 6)")
        return False
    
    otp_code = input("6 chiffres: ").strip()
    if len(otp_code) != 6 or not otp_code.isdigit():
        print("❌ Format!")
        return False
    
    # Remplissage SANS ENTER (Nusuk auto-submit)
    for i, digit in enumerate(otp_code):
        otp_fields[i].clear()
        otp_fields[i].send_keys(digit)
        time.sleep(0.8)  # Auto-advance + stabilise
    
    print("✅ OTP saisi - Attente auto-submit...")
    time.sleep(5)  # Temps pour redirection dashboard
    
    # DASHBOARD (confirmation)
    for attempt in range(10):
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, POST_LOGIN_SELECTOR)))
            print("🎉 DASHBOARD OK!")
            return True
        except:
            print(f"Dashboard retry {attempt+1}/10")
            time.sleep(2)
    
    return True


def keep_session_alive_robust(driver):
    """Keepalive SANS doublon profile"""
    actions = [
        'a[href="/profile/dashboard"]',
        'a[href="/packages"]',
        '#user-profile-menu',  # Dropdown → My Profile
        'a[name="ApplicantMyFamily"]',  # My Family
    ]
    
    print("\n⏰ KEEPALIVE ROBUST v4 - OPTIM")
    cycle = 0
    
    while True:
        cycle += 1
        print(f"\n🔄 Cycle {cycle}")
        
        for selector in actions:
            for retry in range(3):
                try:
                    if selector == '#user-profile-menu':
                        # Dropdown: toggle → My Profile
                        profile_menu = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", profile_menu)
                        driver.execute_script("arguments[0].click();", profile_menu)
                        print("✅ Profile menu ouvert")
                        time.sleep(2)
                        
                        my_profile = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/profile/') and contains(text(), 'My Profile')]"))
                        )
                        driver.execute_script("arguments[0].click();", my_profile)
                        print("✅ My Profile")
                        time.sleep(4)
                        break
                    
                    # Liens directs
                    else:
                        btn = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                        driver.execute_script("arguments[0].click();", btn)
                        print(f"✅ {selector}")
                        time.sleep(4)
                        break
                        
                except:
                    if retry == 2:
                        print(f"❌ Skip {selector}")
                    time.sleep(1)
        
        print(f"😴 {KEEPALIVE_INTERVAL}s...")
        time.sleep(KEEPALIVE_INTERVAL)


def main():
    driver = create_driver()
    try:
        if login_nusuk_hybrid(driver):
            keep_session_alive_robust(driver)
    except KeyboardInterrupt:
        print("👋")
    finally:
        driver.quit()
        print("🔌 Chrome fermé")


if __name__ == "__main__":
    main()
