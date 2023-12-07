# main.py
from scraping import EcommerceScraper

def main():
    url = "https://example.com"
    output_file = "output.csv"
    max_processes = 4

    scraper = EcommerceScraper(url, output_file, max_processes)
    scraper.run()

if __name__ == "__main__":
    main()
