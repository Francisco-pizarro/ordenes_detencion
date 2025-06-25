import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def test_login_fallido_contraseña_incorrecta():
    service = Service(executable_path="./drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get("http://localhost:8000/login")

    # Completar login con credenciales inválidas
    email_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/form/div/div[2]/div[3]/input")
    password_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/form/div/div[3]/div[3]/input")
    boton_ingresar = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/form/div/div[4]/div/button")
    email_input.send_keys("francisco.pizarro@gmail.com")
    password_input.send_keys("12345asas")
    boton_ingresar.click() 

    time.sleep(2)

    mensaje_error = driver.find_element(By.CLASS_NAME, "alert-danger").text
    print("Mensaje detectado:", mensaje_error)

    assert "Correo electrónico o contraseña incorrectos." in mensaje_error

    driver.quit()
