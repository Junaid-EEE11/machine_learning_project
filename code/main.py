from concurrent.futures import ThreadPoolExecutor
   from web_requests import make_realistic_request
   from scraping import scrape_data_with_bs4, scrape_data_with_selenium
   from data_handling import save_data_to_hdf5
   import logging

   logging.basicConfig(level=logging.INFO)
   logger = logging.getLogger(__name__)

   def scrape_and_save_parallel(alibaba_urls):
       data_to_save = {}

       for i, url in enumerate(alibaba_urls):
           bs4_data = scrape_data_with_bs4(url)
           if bs4_data:
               data_to_save[f'bs4_data_{i}'] = bs4_data

       for i, url in enumerate(alibaba_urls):
           selenium_data = scrape_data_with_selenium(url)
           if selenium_data:
               data_to_save[f'selenium_data_{i}'] = selenium_data

       save_data_to_hdf5(data_to_save, config.get('General', 'OutputFilename'))

   if __name__ == "__main__":
       alibaba_urls = ["https://www.alibaba.com/"]
       scrape_and_save_parallel(alibaba_urls)

