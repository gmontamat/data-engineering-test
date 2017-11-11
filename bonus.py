#!/usr/bin/env python

"""
DataScience Data Engineering Test
Parse a corrupted tsv file into a readable one (parallelizable implementation)
"""

import csv
import io
import re


REGEX_ID = r'(1000|[1-9][0-9]{0,2})'
REGEX_FIRSTNAME = r'([^\t]+)?'
REGEX_LASTNAME = r'([^0-9]+)?'
REGEX_ACCOUNT = r'([0-9]{5,6}|[0-9]{4}[-/][0-9]{2}|[0-9]{3}[-/][0-9]{3})'
REGEX_EMAIL = r'([^@^\s]+@[^@^\s]+\.[^@^\s]+)'

REGEX_LINE = REGEX_ID + '\s+' + REGEX_FIRSTNAME + '\s' + REGEX_LASTNAME + '\s' + REGEX_ACCOUNT + '\s+' + REGEX_EMAIL


def fix_tsv(file_path, position, length):
    with io.open(file_path, 'r', encoding='utf-16-le') as fin:
        fin.seek(position)
        data = fin.read(length)
    parsed_data = re.findall(REGEX_LINE, data)  # Use regex to find each line in data
    with open('./data/data_fixed_{}_{}.tsv'.format(position, length), 'wb') as fout:
        csv_writer = csv.writer(fout, delimiter='\t', quotechar='"', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['id', 'first_name', 'last_name', 'account_number', 'email'])
        for record_id, first_name, last_name, account_number, email in parsed_data:
            csv_writer.writerow([
                record_id.strip().encode('utf-8'), first_name.strip().encode('utf-8'),
                last_name.strip().encode('utf-8'), account_number.strip().encode('utf-8'),
                email.strip().encode('utf-8')
            ])


if __name__ == '__main__':
    fix_tsv('./data/data.tsv', 1000, 5000)
