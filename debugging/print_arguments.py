#!/usr/bin/python3
"""
This script print only the arguments without the python file name
"""
import sys

for i in range(1, len(sys.argv)):
    print(sys.argv[i])
    