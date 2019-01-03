#!/usr/bin/env python

''' Tool for converting the MASVS requirements to various formats.

    Usage: ./export.py [--format <csv/xml/json]

    By Bernhard Mueller

    Copyright (c) 2017 OWASP Foundation

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    '''

import argparse
from masvs import MASVS

parser = argparse.ArgumentParser(description='Export the MASVS requirements.')
parser.add_argument('--format', choices=['json', 'xml', 'csv'], default='json')
parser.add_argument('--lang', choices=['es', 'ru', 'en'], default='en')
args = parser.parse_args()

m = MASVS()



if args.format == "csv":
    print(m.to_csv(args.lang))
elif args.format == "xml":
    print(m.to_xml(args.lang))
else:
    print(m.to_json(args.lang))