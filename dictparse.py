#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
# from enum import Enum
from collections import defaultdict

import joblib

HEADER = re.compile('^[A-Z][A-Z\s;\-_]*$')
DEFN = re.compile('^Defn:\s')
FIRST = re.compile('^\d\.\s')
ALPHA = re.compile('^\([a-z]\)\s')
WORD = re.compile('^[A-z]+$')

SKIP_LINES = 27
END_INDICATOR = "End of Project Gutenberg's Webster's Unabridged Dictionary"

def isheader(string):
    return HEADER.match(string) is not None

def headers(string):
    hds = string.split(';')
    return [x.strip() for x in hds]

def isdefn(string):
    return DEFN.match(string) is not None

def isnumber(string):
    return FIRST.match(string) is not None

def isalpha(string):
    return ALPHA.match(string) is not None

def isdefinition(string):
    return isalpha(string) or isnumber(string) or isdefn(string)

def isword(string):
    return WORD.match(string) is not None

def count_chars(dictionary):
    count = 0
    for definitions in dictionary.values():
        count += sum(len(d) for d in definitions)
    return count

def remove_parentheticals(string):
    if not string:
        return string
    stripped = re.sub(r'\([^)]*\)', '', string)
    stripped = re.sub(r'--', '', stripped)
    stripped = re.sub(r'\s\s+', ' ', stripped)
    stripped = re.sub(r'\s+,', ',', stripped)
    return stripped.strip()

def main():

    defs = defaultdict(list)
    defining = False
    last_headers = None
    definition = None
    with open('./pg.txt', 'r') as f:
        # skip first 27 lines
        for _ in range(SKIP_LINES):
            next(f)

        for number, line in enumerate(f):
            if line.startswith(END_INDICATOR):
                break
            number += SKIP_LINES
            line = line.strip()
            # if line == 'ZYMOMETER; ZYMOSIMETER':
            #     import ipdb; ipdb.set_trace()
            if isheader(line):
                if defining:
                    print(isheader(line))
                    print('"{}"'.format(line))
                    print(number)
                assert not defining
                last_headers = [s.strip() for s in line.split(';')]
            elif isdefinition(line):
                definition = remove_parentheticals(definition)
                if definition:
                    for header in last_headers:
                        defs[header].append(definition)

                defining = True
                if isdefn(line):
                    definition = line[6:]
                elif isalpha(line):
                    definition = line[4:]
                elif isnumber(line):
                    definition = line[3:]
                else:
                    assert False
            elif defining:
                if line == '':
                    defining = False
                    # if last_headers is None:
                    #     print(number )
                    #     print(line)
                    assert last_headers is not None
                    definition = remove_parentheticals(definition)
                    if definition:
                        for header in last_headers:
                            # if header == 'ZYMOMETER':
                            #     print(definition)
                            # if header == 'ZYMOSIMETER':
                            #     print(definition)
                            defs[header].append(definition)
                    definition = None
                else:
                    assert definition is not None
                    definition += ' ' + line

    print('Character count is {}.'.format(count_chars(defs)))

    # print(defs['GAPER'])

    joblib.dump(defs, 'definitions.pkl')


if __name__ == "__main__":
    main()
