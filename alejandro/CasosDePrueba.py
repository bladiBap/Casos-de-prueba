import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time, random

class tester:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def save_screenshot(self, directory, image_id):
        base_directory = "reports/"
        if not os.path.exists(os.path.abspath(base_directory) + "/" + directory):
            os.makedirs(os.path.abspath(base_directory) + "/" + directory)
        self.driver.save_screenshot(base_directory + directory + "/" + str(image_id) + ".png")

    def scroll_to_bottom(self):
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(3)

    def login(self):
        self.driver.get("https://admin.tartesain.com/")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email'))
        ).send_keys("admin@gmail.com")
        self.driver.find_element(By.ID, "Password").send_keys("kakawate")
        self.driver.find_element(By.ID, "btn-login").click()

    def test_create_product(self):
        screenshot_id = 1
        test_directory = "create_product"
        link_products = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'link-products'))
        )
        self.save_screenshot(test_directory, screenshot_id)
        link_products.click()
        screenshot_id += 1

        btn_create_product = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@href="/productos/crear"]'))
        )
        self.save_screenshot(test_directory, screenshot_id)
        btn_create_product.click()
        screenshot_id += 1

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'name'))
        ).send_keys("Producto de prueba")

        self.driver.find_element(By.ID, "description").send_keys("Descripcion de prueba")
        self.driver.find_element(By.ID, "price").send_keys("5")
        self.save_screenshot(test_directory, screenshot_id)
        screenshot_id += 1

        self.driver.find_element(By.XPATH, '//*[@for="flexSwitchCheck1"]').click()
        self.save_screenshot(test_directory, screenshot_id)
        screenshot_id += 1

        image_path = os.path.abspath("images/placeholder.png")
        self.driver.find_element(By.ID, "icon").send_keys(image_path)
        self.driver.find_element(By.ID, "input-gallery").send_keys(image_path)
        self.save_screenshot(test_directory, screenshot_id)
        screenshot_id += 1       

        self.driver.find_element(By.ID, "btn-save").click()
        self.scroll_to_bottom()
        self.save_screenshot(test_directory, screenshot_id)

    def test_update_product(self):
        screenshot_id = 1
        test_directory = "update_product"
        nombre_producto = "Producto de prueba"
        btn_edit_product = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//td[text()='{nombre_producto}']/following-sibling::td//a[contains(@class, 'link-edit')]"))
        )
        self.save_screenshot(test_directory, screenshot_id)
        screenshot_id += 1
        btn_edit_product.click()
        
        name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'name'))
        )

        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.find_element(By.ID, "name").get_attribute("value")) != 0
        )

        self.save_screenshot(test_directory, screenshot_id)
        screenshot_id += 1

        name_input.clear()
        name_input.send_keys("Producto de prueba actualizado")

        description_input = self.driver.find_element(By.ID, "description")
        description_input.clear()
        description_input.send_keys("Descripcion de prueba actualizada")

        price_input = self.driver.find_element(By.ID, "price")
        price_input.clear()
        price_input.send_keys("10")

        self.driver.find_element(By.XPATH, '//*[@for="flexSwitchCheck1"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@for="flexSwitchCheck2"]').click()

        self.save_screenshot(test_directory, screenshot_id)
        screenshot_id += 1

        self.driver.find_element(By.ID, "btn-save").click()
        self.scroll_to_bottom()
        self.save_screenshot(test_directory, screenshot_id)

    def test_delete_product(self):
        screenshot_id = 1
        test_directory = "delete_product"
        nombre_producto = "Producto de prueba actualizado"
        btn_delete_product = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//td[text()='{nombre_producto}']/following-sibling::td//button[contains(@class, 'btn-delete')]"))
        )
        self.save_screenshot(test_directory, screenshot_id)
        screenshot_id += 1
        btn_delete_product.click()

        alert = self.driver.switch_to.alert
        alert.accept()
        self.scroll_to_bottom()
        self.save_screenshot(test_directory, screenshot_id)

    def test_create_admin(self, phone_admin):
        screenshot_id = 1
        test_directory = "create_admin"
        self.driver.get("https://admin.tartesain.com")

        link_admins = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'link-admins'))
        )
        self.save_screenshot(test_directory, screenshot_id)
        link_admins.click()
        screenshot_id += 1

        btn_create_admin = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@href="/admins/crear"]'))
        )
        self.save_screenshot(test_directory, screenshot_id)
        btn_create_admin.click()
        screenshot_id += 1

        name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'name'))
        )
        self.save_screenshot(test_directory, screenshot_id)
        screenshot_id += 1

        name_input.send_keys("Admin")
        self.driver.find_element(By.ID, "lastName").send_keys("de prueba")

        email_admin = "admin" + str(time.time()) + "@gmail.com"
        self.driver.find_element(By.ID, "email").send_keys(email_admin)
        self.driver.find_element(By.ID, "password").send_keys("test1234")
        self.driver.find_element(By.ID, "passwordConfirmation").send_keys("test1234")
        self.driver.find_element(By.ID, "phone").send_keys(phone_admin)
        self.save_screenshot(test_directory, screenshot_id)
        screenshot_id += 1

        role_select = self.driver.find_element(By.ID, "role")
        select = Select(role_select)
        select.select_by_visible_text("Administrador")
        self.save_screenshot(test_directory, screenshot_id)
        screenshot_id += 1

        btn_save = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn-save"))
        )
        btn_save.click()
        self.scroll_to_bottom()
        self.save_screenshot(test_directory, screenshot_id)

    def test_update_admin(self, phone_admin):
        screenshot_id = 1
        test_directory = "update_admin"
        
        btn_edit_admin = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//td[text()='{phone_admin}']/following-sibling::td//button[contains(@id, 'btn-edit')]"))
        )
        self.save_screenshot(test_directory, screenshot_id)
        screenshot_id += 1
        btn_edit_admin.click()

        name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'name'))
        )

        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.find_element(By.ID, "name").get_attribute("value")) != 0
        )

        self.save_screenshot(test_directory, screenshot_id)
        screenshot_id += 1

        name_input.clear()
        name_input.send_keys("Admin")

        last_name_input = self.driver.find_element(By.ID, "lastName")
        last_name_input.clear()
        last_name_input.send_keys("de prueba actualizado")

        phone_input = self.driver.find_element(By.ID, "phone")
        phone_input.clear()
        phone_input.send_keys(phone_admin)

        self.save_screenshot(test_directory, screenshot_id)
        screenshot_id += 1

        self.driver.find_element(By.ID, "btn-save").click()
        self.scroll_to_bottom()
        self.save_screenshot(test_directory, screenshot_id)

    def test_delete_admin(self, phone_admin):
        screenshot_id = 1
        test_directory = "delete_admin"

        btn_delete_admin = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//td[text()='{phone_admin}']/following-sibling::td//button[contains(@id, 'btn-delete')]"))
        )
        self.save_screenshot(test_directory, screenshot_id)
        screenshot_id += 1
        btn_delete_admin.click()

        alert = self.driver.switch_to.alert
        alert.accept()
        self.scroll_to_bottom()
        self.save_screenshot(test_directory, screenshot_id)

    def execute(self):
        self.login()
        self.test_create_product()
        self.test_update_product()
        self.test_delete_product()
        phone_admin = "7" + str(random.randint(1000000, 9999999))
        self.test_create_admin(phone_admin=phone_admin)
        self.test_update_admin(phone_admin=phone_admin)
        self.test_delete_admin(phone_admin=phone_admin)
        self.driver.quit()

if __name__ == '__main__':
        tester = tester()
        tester.execute()



