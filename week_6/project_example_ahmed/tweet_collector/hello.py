
import time
import sys
import logging

while True:
    sys.stderr.write(f"STDERR: {time.asctime()}   hello world\n")
    logging.critical("LOGGING: hello world")
    time.sleep(10)
