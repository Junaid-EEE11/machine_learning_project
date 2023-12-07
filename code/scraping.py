# scraper.py
import multiprocessing
from data_saver import save_to_csv
from ecommerce_parser import EcommerceParser

class EcommerceScraper:
    def __init__(self, url, output_file, max_processes=1):
        self.url = url
        self.output_file = output_file
        self.max_processes = max_processes

    def run(self):
        data = self.scrape()
        save_to_csv(data, self.output_file)

    def scrape(self):
        parser = EcommerceParser(self.url)
        product_links = parser.get_product_links()

        with multiprocessing.Pool(self.max_processes) as pool:
            data = pool.map(self.fetch_product_data, product_links)

        return data

    def fetch_product_data(self, product_link):
        try:
            parser = EcommerceParser(product_link)
            product_data = parser.parse_product_data()
            return product_data
        except Exception as e:
            print(f"Error fetching data for {product_link}: {e}")
            return None

# Add error handling, waiting, and other features as needed
