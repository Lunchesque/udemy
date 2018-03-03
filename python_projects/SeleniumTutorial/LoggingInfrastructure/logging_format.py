
import logging

logging.basicConfig(filename='test.log',format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S', level=logging.DEBUG)

logging.warning("warning message")
logging.info("info message")
logging.error("error message")
