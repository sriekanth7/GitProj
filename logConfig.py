import logging
logger = logging.getLogger("Foo")


# create a file handler
handler = logging.FileHandler('myLog.log')
handler.setLevel(logging.DEBUG)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)


# add the handlers to the logger
logger.addHandler(handler)

logger.info('logging initialized')
