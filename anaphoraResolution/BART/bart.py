#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Arne Neumann <pybart.programming@arne.cl>

"""
Simple Python wrapper for BART (Beautiful Anaphora Resolution Toolkit).

Usage::

    bart.py input.txt output.xml
"""

import sys
import os
import urlparse
import requests

BART_SERVER = 'http://localhost:8125'


def get_coreferences(input_filepath, host=BART_SERVER):
    """
    Takes a plain text file as input, pushes it to a running BART
    coreference server and returns a string that contains an inline XML
    representation of the input with coreferences added.
        """
    assert os.path.isfile(input_filepath), \
        "File doesn't exist: {}".format(input_filepath)
    with open(input_filepath, 'r') as input_file:
        post_url = urlparse.urljoin(host, '/BARTDemo/ShowText/process/')
        response = requests.post(post_url, input_file)
    return response.content


if __name__ == '__main__':
    with open(sys.argv[1],'r') as  input_file:
        lines=input_file.readlines()
    count=0
    while count< len(lines):
        name=sys.argv[1]+str(count)
        with open('Input/'+,'w') as temp_file:
            temp_file.write(lines[count])
        count+=1
    if len(sys.argv) != 3:
        sys.stderr.write(
            'Usage: {0} input_file output_file\n'.format(sys.argv[0]))
        sys.exit(1)
    else:
        for filename in sorted(os.listdir('Input')):
        
            input_filepath = 'Input/'+filename
            output_string = get_coreferences(input_filepath)

            output_filepath = 'Output/'+filename+'.xml'
            with open(output_filepath, 'w') as output_file:
                output_file.write(output_string)
