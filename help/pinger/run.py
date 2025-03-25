#!/usr/bin/env python3

import logging
import random
import time

while True:

    number = random.randrange(0, 4)

    if number == 0:
        logging.info('hi!!')
    elif number == 1:
        logging.warning('boroda')
    elif number == 2:
        logging.error('error!!!!')
    elif number == 3:
        logging.exception(Exception('exception'))

    time.sleep(1)