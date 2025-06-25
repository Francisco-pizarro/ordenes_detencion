import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def test_login_muestra_nombre_usuario():
    service = Service(executable_path="./drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("http://localhost:8000/login")

        # Localizando elementos por XPATH según tu estructura HTML:
        email_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/form/div/div[2]/div[3]/input")
        password_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/form/div/div[3]/div[3]/input")
        boton_ingresar = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/form/div/div[4]/div/button")

        # Completar y enviar el formulario
        email_input.send_keys("francisco.pizarro@gmail.com")
        password_input.send_keys("12345678")
        boton_ingresar.click() 

        time.sleep(2)

        body_text = driver.page_source
        assert "Francisco Pizarro" in body_text or "Bienvenid@" in body_text

    finally:
        driver.quit()
