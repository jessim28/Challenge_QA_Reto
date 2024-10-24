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
        self.driver.get("http://localhost:4000/login")
        self.driver.maximize_window()

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=5):
        time.sleep(round(timeout))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    # Test 1 Verificar el login con correo válido y contraseña válida
    def test_login_successful(self, send=None):
        t = 2

        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("jessica@gmail.com")
        time.sleep(t)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("password123")
        time.sleep(t)
        self.driver.find_element(By.XPATH, "//button[@id='login']").click()
        time.sleep(t)

        # Verificar que aparece un mensaje de error
        error_message = self.driver.find_element(By.XPATH, "// label[ @ id = 'msg']").text
        assert error_message == "LOGIN VALID"

    # Test 2 Verificar el Login con correo sin "@"
    def test_login_invalidad_email(self, send=None):
            t = 2

            self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("jessicagmail.com")
            time.sleep(t)
            self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("password123")
            time.sleep(t)
            self.driver.find_element(By.XPATH, "//button[@id='login']").click()
            time.sleep(t)

            # Verificar que aparece un mensaje de error por email incorrecto
            error_message = self.driver.find_element(By.XPATH, "// label[ @ id = 'msg']").text
            assert error_message == "LOGIN VALID"

    # Test 3 Verificar el Login con contraseña (menor a 5 caracteres)
    def test_login_invalidad_password(self, send=None):
            t = 2

            self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("challenge@gmail.com")
            time.sleep(t)
            self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123")
            time.sleep(t)
            self.driver.find_element(By.XPATH, "//button[@id='login']").click()
            time.sleep(t)

            # Verificar que aparece un mensaje de error por email incorrecto
            error_message = self.driver.find_element(By.XPATH, "// label[ @ id = 'msg']").text
            assert error_message == "LOGIN VALID"

    # Test 4 Verificar Login sin correo
    def test_login_invalidad_email(self, send=None):
            t = 2

            self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("")
            time.sleep(t)
            self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("abcdef1")
            time.sleep(t)
            self.driver.find_element(By.XPATH, "//button[@id='login']").click()
            time.sleep(t)

            # Verificar que aparece un mensaje de error
            error_message = self.driver.find_element(By.XPATH, "// label[ @ id = 'msg']").text
            assert error_message == "REQUIRED"

    # Test 5 Verificar Login sin contraseña
    def test_login_invalidad_password(self, send=None):
            t = 2

            self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("jessica@gmail.com")
            time.sleep(t)
            self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("")
            time.sleep(t)
            self.driver.find_element(By.XPATH, "//button[@id='login']").click()
            time.sleep(t)

            # Verificar que aparece un mensaje de error
            error_message = self.driver.find_element(By.XPATH, "// label[ @ id = 'msg']").text
            assert error_message == "REQUIRED"

    #Test 6 Verificar Login con campos inválidos (correo sin "@" y contraseña menor a 5 caracteres
    def test_login_invalidad_both(self, send=None):
        t = 2

        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("usuarioexample.com")
        time.sleep(t)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("ab1")
        time.sleep(t)
        self.driver.find_element(By.XPATH, "//button[@id='login']").click()
        time.sleep(t)

        # Verificar que aparece un mensaje de error
        error_message = self.driver.find_element(By.XPATH, "// label[ @ id = 'msg']").text
        assert error_message == "LOGIN VALID"