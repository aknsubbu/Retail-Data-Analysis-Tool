import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """Function to set up a logger; can be used across all subdirectories."""
    

    logger = logging.getLogger(name)
    logger.setLevel(level)
    

    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))
    
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger