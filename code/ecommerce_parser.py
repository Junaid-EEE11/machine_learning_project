# ecommerce_parser.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class EcommerceParser:
    def __init__(self, url):
        self.url = url;
        self.options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.driver = webdriver.Firefox(executable_path=r'C:\pythone\geckodriver.exe', options=options)

    def get_product_links(self, url):
        self.driver.get(url)

        # Scroll to the end of the page
        self.scroll_to_end()

        # Wait for product links to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href and contains(@href, 'product_detail')]"))
        )

        # Get all links with "product_detail" in the URL
        product_links = [a.get_attribute('href') for a in self.driver.find_elements(By.XPATH, "//a[@href and contains(@href, 'product_detail')]")]

        return product_links

    def scroll_to_end(self):
        # Scroll to the end of the page
        while True:
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            # Add a delay or wait for the page to load more content
            # You may need to adjust the sleep duration based on the website
            time.sleep(2)
            # Check if you have reached the end of the page
            if self.is_end_of_page():
                break

    def is_end_of_page(self):
        # Implement logic to check if you have reached the end of the page
        # For example, compare the current and previous page heights
        # If they are the same, you may have reached the end
        current_height = self.driver.execute_script("return document.body.scrollHeight;")
        time.sleep(2)  # Add a delay to ensure the page has loaded
        new_height = self.driver.execute_script("return document.body.scrollHeight;")
        return current_height == new_height


    def parse_product_data(self):
        # Wait for the product details to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-details']"))
        )

        # Find the product details element
        product_details_element = self.driver.find_element(By.XPATH, "//div[@class='product-details']")

        # Extract all text data from the product details element
        text_data_list = self.extract_all_text(product_details_element)

        return text_data_list

    def extract_all_text(self, element):
        # Recursively extract all text data from an element and its children
        text_data_list = []

        if element.text:
            text_data_list.append(element.text)

        for child_element in element.find_elements(By.XPATH, ".//*"):
            if child_element.text:
                text_data_list.append(child_element.text)

        return text_data_list
