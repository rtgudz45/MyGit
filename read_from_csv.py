import os
import csv
import requests
import argparse
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S',level = logging.DEBUG)
a = 'sasa'


def process_emails(args):

        if not os.path.isfile(args.input_file):
                logging.info('No input file provided!!..Exiting...')
                return

        with open(args.input_file,'rb') as input_file:
                rows = csv.DictReader(input_file)
                for row in rows:
                        logging.info('Email is %s'%row.get('EMAIL'))





def main():
        logging.info('Inside main....Wakanda forever!!')
        parser = argparse.ArgumentParser(description='Script to read emails from a csv file and process them')
        parser.add_argument( '-i', '--input_file',help='input csv file having emails')

        args = parser.parse_args()

        process_emails(args)
        

if __name__ == '__main__':
        main()

