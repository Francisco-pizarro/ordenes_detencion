import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def test_login_exitoso():
    service = Service(executable_path="./drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get("http://localhost:8000/login")

    email_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/form/div/div[2]/div[3]/input")
    password_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/form/div/div[3]/div[3]/input")
    boton_ingresar = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/form/div/div[4]/div/button")
    email_input.send_keys("francisco.pizarro@gmail.com")
    password_input.send_keys("12345678")
    boton_ingresar.click() 

    time.sleep(2)

    assert "Bienvenido a la ficha de alerta ORD" in driver.page_source or driver.current_url != "http://localhost:8000/login"
    driver.quit()
