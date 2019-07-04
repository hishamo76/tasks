import logging
import platform


import argparse
p = argparse.ArgumentParser()
p.add_argument("--log")

args = p.parse_args()
loglevel = args.log



logging.basicConfig(level=getattr(logging, loglevel.upper(), None))

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
