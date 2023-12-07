import h5py
import logging
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_data_to_hdf5(data, filename):
    try:
        with h5py.File(filename, 'a+') as hdf_file:
            for key, value in data.items():
                hdf_file.create_dataset(key, data=value)
    except Exception as e:
        logger.error(f"Error saving data to HDF5: {e}")
