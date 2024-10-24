from asyncio import timeout
from idlelib import browser
from lib2to3.pgen2 import driver
from select import select
from telnetlib import EC

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Testchallengeqa():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}
        self.driver.get("http://localhost:4000/register")
        self.driver.maximize_window()

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=5):
        time.sleep(round(timeout))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    # Test 1 Verificar el registro exitoso con correo y contraseña válidos.
    def test_register_successful(self, send=None):
        t = 2

        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("jessica@gmail.com")
        time.sleep(t)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("password123")
        time.sleep(t)
        self.driver.find_element(By.XPATH, "//button[@id='register']").click()
        time.sleep(t)

   # Test 2 Verificar el registro con correo sin "@"
    def test_register_invalidad_email(self, send=None):
        t = 2

        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("jessicagmail.com")
        time.sleep(t)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("password123")
        time.sleep(t)
        self.driver.find_element(By.XPATH, "//button[@id='register']").click()
        time.sleep(t)

        # Verificar que aparece un mensaje de error por email incorrecto
        error_message = self.driver.find_element(By.XPATH, "// label[ @ id = 'msg']").text
        assert error_message == "INVALID"

    # Test 3 Verificar el registro con contraseña menor a 5 caracteres
    def test_register_invalidad_password(self, send=None):
        t = 2

        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("challenge@gmail.com")
        time.sleep(t)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123")
        time.sleep(t)
        self.driver.find_element(By.XPATH, "//button[@id='register']").click()
        time.sleep(t)

        # Verificar que aparece un mensaje de error por email incorrecto
        error_message = self.driver.find_element(By.XPATH, "// label[ @ id = 'msg']").text
        assert error_message == "INVALID"

    # Test 4 VVerificar el registro sin correo
    def test_register_empty_email(self, send=None):
        t = 2

        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("")
        time.sleep(t)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("password123")
        time.sleep(t)
        self.driver.find_element(By.XPATH, "//button[@id='register']").click()
        time.sleep(t)

        # Verificar que aparece un mensaje de error
        error_message = self.driver.find_element(By.XPATH, "// label[ @ id = 'msg']").text
        assert error_message == "REQUIRED"

    # Tets 5 Registro sin contraseña
    def test_register_empty_password(self, send=None):
        t =2

        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("challenge@gmail.com")
        time.sleep(t)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("")
        time.sleep(t)
        self.driver.find_element(By.XPATH, "//button[@id='register']").click()
        time.sleep(t)

        # Verificar que aparece un mensaje de error
        error_message = self.driver.find_element(By.XPATH, "// label[ @ id = 'msg']").text
        assert error_message == "REQUIRED"

    # Test 6 Verificar el registro con campos inválidos (correo sin "@" y contraseña menor a 5 caracteres)
    def test_register_invalidad_both(self, send=None):
        t = 2

        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("challengegmail.com")
        time.sleep(t)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("12a")
        time.sleep(t)
        self.driver.find_element(By.XPATH, "//button[@id='register']").click()
        time.sleep(t)

        # Verificar que aparece un mensaje de error por email incorrecto
        error_message = self.driver.find_element(By.XPATH, "// label[ @ id = 'msg']").text
        assert error_message == "INVALID"