import csv
import requests
import argparse
import logging

logging.basicConfig(level = logging.DEBUG)
a = 'sasa'

def main():
        print 'Hello main , '+a

        logging.info('The value of a is %s'%a)

        

if __name__ == '__main__':
        main()

