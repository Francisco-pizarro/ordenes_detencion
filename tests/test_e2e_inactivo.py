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

        # XPath según tu HTML
        email_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/form/div/div[2]/div[3]/input")
        password_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/form/div/div[3]/div[3]/input")
        boton_ingresar = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/form/div/div[4]/div/button")

        # Completar el formulario
        email_input.send_keys("inactivo@test.cl")
        password_input.send_keys("Clave123")
        boton_ingresar.click()

        time.sleep(2)

        # Verificar que el mensaje de error por cuenta inactiva aparezca
        body_text = driver.page_source
        assert "su cuenta se encuentra inactiva" in body_text.lower()

    finally:
        driver.quit()
