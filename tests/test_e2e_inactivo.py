import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_login_usuario_inactivo():
    Usuario = get_user_model()
    Usuario.objects.create_user(
        email="inactivo@test.cl",
        password="Clave123",
        is_active=False,
        first_name="Usuario",
        last_name="Inactivo"
    )

    service = Service(executable_path="./drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("http://localhost:8000/login")

       
        email_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/form/div/div[2]/div[3]/input")
        password_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/form/div/div[3]/div[3]/input")
        boton_ingresar = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/form/div/div[4]/div/button")

    
        email_input.send_keys("inactivo@test.cl")
        password_input.send_keys("Clave123")
        boton_ingresar.click()

        time.sleep(2)

       
        body_text = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]")
        assert body_text.text=="Su cuenta se encuentra inactiva. Contacte al administrador."

    finally:
        driver.quit()
