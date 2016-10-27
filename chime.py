#!/usr/bin/python

# Chime Markdown extraction file

import sys

# determines if the text is an actual version
def is_version(text):
    return '#' in text

# obtains the version from the text
def get_version(text):
    return text.replace('# ', '').strip()

file_path = sys.argv[1] + sys.argv[2]
command = sys.argv[3]
data=""
is_text=0
with open(file_path) as f:
    for line in f:
        if is_text and is_version(line):
            break
        if not is_text and is_version(line) and command == 'version':
            data = get_version(line)
            break
        if not is_version(line) and command == 'text':
            is_text = 1
            data = data + line

print data.rstrip().lstrip()
