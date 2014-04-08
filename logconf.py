import glob
import logging
import logging.handlers

LOG_FILENAME = 'mylog.txt'

# Set up a specific logger with our desired output level
my_logger = logging.FileHandler('myLog.log')
my_logger.setLevel(logging.DEBUG)
# set formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
my_logger.setFormatter(formatter)
# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=2000, backupCount=5)

my_logger.addHandler(handler)

# Log some messages
for i in range(20):
    my_logger.debug('i = %d' % i)


