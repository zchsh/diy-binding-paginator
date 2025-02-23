import sys
import argparse

parser = argparse.ArgumentParser(
        prog='ArgumentParserTest',
        description='Tests parsing arguments')

parser.add_argument('-i', '--input-file')
parser.add_argument('-o', '--output-file')

args = parser.parse_args()
print(args)
