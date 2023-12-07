# ecommerce_parser.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EcommerceParser:
    def __init__(self, url):
        self.url = url;
        self.options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.driver = webdriver.Firefox(executable_path=r'C:\pythone\geckodriver.exe', options=options)

    def get_product_links(self):
        self.driver.get(self.url)

        # Implement logic to wait for product links to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='product-link']"))
        )

        # Get product links from the main page
        product_links = [a.get_attribute('href') for a in self.driver.find_elements(By.XPATH, "//a[@class='product-link']")]

        return product_links

    def parse_product_data(self):
        # Implement logic to extract product data from the product page
        product_data = {
            'name': self.extract_text(By.XPATH, "//h1[@class='product-name']"),
            'price': self.extract_text(By.XPATH, "//span[@class='product-price']"),
            'description': self.extract_text(By.XPATH, "//div[@class='product-description']")
        }

        return product_data

    def extract_text(self, by, locator):
        element = self.driver.find_element(by, locator)
        return element.text if element else None
