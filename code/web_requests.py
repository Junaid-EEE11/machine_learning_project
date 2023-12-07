import requests
import time
import logging
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def make_realistic_request(url):
    try:
        time.sleep(1)
        headers = {"User-Agent": config.get('Request', 'User-Agent')}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.content
    except requests.exceptions.Timeout:
           logger.error(f"Request to {url} timed out.")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error making request to {url}: {e}")
        return None
