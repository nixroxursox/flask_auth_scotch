# logging.py


import logging
import auxiliary_module

# create logger with 'spam_application'
logger = logging.getLogger("spam_application")
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
`````fh = logging.FileHandler("spam.log")`````
fh.setLevel(logging.DEBUG)
# create console handler with a higher log levelname
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
